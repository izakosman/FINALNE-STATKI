import pygame
import numpy as np
import random as ran
import sys
import _thread



pygame.init()


# __________________________________________________________________________________________________________________
#                                         GLOWNE OKNO GRY                                                           |
# __________________________________________________________________________________________________________________|
pokaz_gre_szerokosc = 1000
pokaz_gre_wysokosc=800
pokaz_gre=pygame.display.set_mode((pokaz_gre_szerokosc,pokaz_gre_wysokosc))
pygame.display.set_caption("Gra  w statki - I.Kosman")
clock = pygame.time.Clock()

# __________________________________________________________________________________________________________________
#                                         PLIKI ZEW I KOLORY                                                        |
# __________________________________________________________________________________________________________________|
#kolory
black=(0,0,0)
white=(255,255,255)
white2=(247,247,247)
white3=(139,123,139)
blueocean=(150,205,205)
falsered=((255,48,48))
gray1=(199,199,199)
gray2=(232,232,232)
gray3=(220,220,220)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#obrazy
planszatekst=pygame.image.load('planszatekst.png')
czat=pygame.image.load('czat.png')
czat2=pygame.image.load('czat2.png')
plansza=pygame.image.load('plansza.png')
wyjdz=pygame.image.load('wyjdz.png')


# __________________________________________________________________________________________________________________
#                                          TEKST/CZCIONKA                                                           |
# __________________________________________________________________________________________________________________|
font = pygame.font.Font('Pokemon GB.ttf', 18)
text1 = font.render('Twoja Plansza:', True, black, gray1)
text2 = font.render('Plansza \n Przeciwnika:', True, black, gray1)
text3 = font.render('Czat:', True, black, gray1)
text1rect = text1.get_rect()
text1rect.center = (250, 50)
text2rect = text2.get_rect()
text2rect.center = (740, 50)
text3rect = text3.get_rect()
text3rect.center = (500, 495)



# __________________________________________________________________________________________________________________
#                                           PLANSZA PETLA                                                           |
# __________________________________________________________________________________________________________________|
szerokosc_plansza = 30
wysokosc_plansza = 30
przerwy_kratki = 2                                            # margines miedzy kazda z komorek planszy

# ______________________________________________________________________STWORZ 2 WYMIAROWY ARRAY

plansza_klik = []
for wiersz in range(10):                                      # czyli chcemy miec 10 wierszy w naszym array
                                                              # pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
    plansza_klik.append([])
    for kolumna in range(10):
        plansza_klik[wiersz].append(0)                        #tam gdzie jest zero zmien na rzeczywisty wiersz


    print('plansza klik: ',plansza_klik)
plansza_klik[1][5] = 0                                        # scal kolumne 1 i wiersz 5 do 1 (bo zaczyna sie od 0)

print('plansza klik: ', plansza_klik)

def plansza_klikaj():
    done = False

    # ________________________________________________________________________POBIERANIE KOORDYNATOW Z PLANSZY

    while not done:
        for event in pygame.event.get():                                           # gdy uzytkownik cos zrobi
            if event.type == pygame.QUIT:                                          # jesli kliknie wyjdz
                done = True                                                        # zaznacz ze skoncz prace

            elif event.type == pygame.MOUSEBUTTONDOWN:                             # gdy uzytkownik kliknie pobierz
                pos = pygame.mouse.get_pos()                                       # koordynaty kursora
                kolumna = pos[0] //  ( szerokosc_plansza + przerwy_kratki  )         # zmien kolumne i y na koordynaty typowe dla planszy
                wiersz = pos[1] // ( wysokosc_plansza + przerwy_kratki )           # czyli zamiast 123213,93287437 bedzie np 1 1
                plansza_klik[wiersz][kolumna] = 1                                  # stworz jedna lokacje z wiersza i kolumny
                print("Click ", pos, "koordynaty planszy: ", wiersz, kolumna)


        # ______________________________________________________________________RYSOWANIE PLANSZY

        for wiersz in range(10):                                                 #dla 10 wierszy
            for kolumna in range(10):                                            #dla 10 kolumn
                kolor = gray3                                                    #kolor ppol
                if plansza_klik[wiersz][kolumna] == 1:
                    kolor = GREEN
                pygame.draw.rect(pokaz_gre, kolor,[(((  przerwy_kratki + szerokosc_plansza ) * kolumna + przerwy_kratki + 580 )),
                                  (((  przerwy_kratki + wysokosc_plansza  ) * wiersz + przerwy_kratki +100  )),
                                       szerokosc_plansza,wysokosc_plansza])


                                                                                # Limit to 60 frames na sekunde
        clock.tick(60)

                                                                                # update  screen
        pygame.display.flip()

'''
# __________________________________________________________________________________________________________________
#                                           TWOJA PLANSZA                                                           |
# __________________________________________________________________________________________________________________|
twojestatki = (np.load('GRACZ_STATKI.npy', mmap_mode='r'))

twojapl=[]

def twoja_plansza():
    done = False

    for wiersz in range(10):                                  #czyli chcemy miec 10 wierszy w naszym array
                                                             #pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
        twojapl.append([])
        for kolumna in range(10):
            twojapl[wiersz].append(0)

    twojapl[1][5] = 0                                            ## scal kolumne 1 i wiersz 5 do 1 (bo zaczyna sie od 0)

    pygame.init()
    print(twojapl)
    twojaplansza = twojestatki

    while not done:
        for event in pygame.event.get():                                    # gdy uzytkownik cos zrobi
            if event.type == pygame.QUIT:                                   # jesli kliknie wyjdz
                done = True                                                 # zaznacz ze skoncz prace

        for wiersz in range(10):
            for kolumna in range(10):
                kolor = BLACK
                if plansza[wiersz][kolumna] != 0:
                    kolor = GREEN
                pygame.draw.rect(pokaz_gre,kolor,[(przerwy_kratki + szerokosc_plansza) * kolumna + przerwy_kratki,(przerwy_kratki + wysokosc_plansza) * wiersz + przerwy_kratki, wysokosc_plansza, wysokosc_plansza])

        # Limit to 60 frames na sekunde
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
'''
# __________________________________________________________________________________________________________________
#                                            GLOWNA PETLA                                                           |
# __________________________________________________________________________________________________________________|

def pvp():

    pokaz_gre = pygame.display.set_mode((pokaz_gre_szerokosc, pokaz_gre_wysokosc))
    pygame.display.set_caption("Gra  w statki - I.Kosman")
    clock = pygame.time.Clock()
                                                                            # wypelnienie tlo intro
    tlo = pygame.Surface(pokaz_gre.get_size())
    tlo = tlo.convert()
    tlo.fill(white3)

                                                                            # blit czyliwszyskoscalamy
    pokaz_gre.blit(tlo, (0, 0))
    pygame.display.flip()###
    print('wybrano  pvp')

    gamemen = True
    while gamemen:

        pokaz_gre.fill(white3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse=pygame.mouse.get_pos()
        klik=pygame.mouse.get_pressed()
        while True:

            pokaz_gre.fill(white3)

            pokaz_gre.blit(planszatekst,(40,26))
            pokaz_gre.blit(planszatekst, (520, 26))
            pokaz_gre.blit(plansza, (520, 86))
            pokaz_gre.blit(plansza, (40, 86))
            pokaz_gre.blit(czat,(40,470))
            pokaz_gre.blit(czat2,(40,525))
            pokaz_gre.blit(wyjdz, (430, 730))
            pokaz_gre.blit(text1, text1rect)
            pokaz_gre.blit(text2, text2rect)
            pokaz_gre.blit(text3, text3rect)
            pokaz_gre.blit(plansza_klikaj())






            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                pygame.display.update()


pvp()