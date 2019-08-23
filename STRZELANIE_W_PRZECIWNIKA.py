import pygame
import sys
import numpy
import os
import numpy as np
import random as ran




planszaprzeciwnika = (np.load('PRZECIWNIK_PLANSZA.npy', mmap_mode='r'))

print(planszaprzeciwnika)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
gray1=(199,199,199)
gray2=(232,232,232)
gray3=(220,220,220)


#_______________________________________________________wysokosc i szerokosc planszy
szerokosc_plansza = 30
wysokosc_plansza = 30

#_______________________________________________________margines miedzy kazda z komorek planszy
przerwy_kratki = 2



#__________________________________________________________________________________________
#                2 wymiarowy array z zaladowaniem twojej planszy                           |
#__________________________________________________________________________________________|

plansza=[]

for wiersz in range(10):                                  #czyli chcemy miec 10 wierszy w naszym array
                                                         #pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
    plansza.append([])
    for kolumna in range(10):
        plansza[wiersz].append(0)

plansza[1][5] = 0                                            ## scal kolumne 1 i wiersz 5 do 1 (bo zaczyna sie od 0)

pygame.init()
print(plansza)

plansza2=[]

for wieersz in range(10):                                  #czyli chcemy miec 10 wierszy w naszym array
                                                         #pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
    plansza2.append([])
    for kolumnaa in range(10):
        plansza2[wieersz].append(0)

plansza2[1][5] = 0
plansza2=planszaprzeciwnika

print(plansza)

#__________________________________________________________________________________________
#                                                OKNO                                      |
#__________________________________________________________________________________________|
# szerokosc i wysokosc okienka
WINDOW_SIZE = [323, 323]
screen = pygame.display.set_mode(WINDOW_SIZE)
# nazwa okna
pygame.display.set_caption("PLANSZA PRZECIWNIKA")
# petla do momentu klikniecia
done = False

clock = pygame.time.Clock()
print('plansza2 ',plansza2[1][1])
#__________________________________________________________________________________________
#                             GLOWNA PETLA                                                 |
#__________________________________________________________________________________________|
while not done:
    for event in pygame.event.get():                                    # gdy uzytkownik cos zrobi
        if event.type == pygame.QUIT:                                   # jesli kliknie wyjdz
            done = True                                                 # zaznacz ze skoncz prace

        elif event.type == pygame.MOUSEBUTTONDOWN:                      # gdy uzytkownik kliknie pobierz
            pos = pygame.mouse.get_pos()                                # koordynaty kursora

            kolumna = pos[0] // (szerokosc_plansza + przerwy_kratki)    #zmien kolumne i y na koordynaty typowe dla planszy
            wiersz = pos[1] // (wysokosc_plansza + przerwy_kratki)      # czyli zamiast 123213,93287437 bedzie np 1 1
            plansza[wiersz][kolumna] = 1                                    # stworz jedna lokacje z wiersza i kolumny
            print("Click ", pos, "koordynaty planszy: ", wiersz, kolumna)

    # tutaj tlo planszy
    screen.fill(gray3)

    for wiersz in range(10):
        for kolumna in range(10):
            if plansza[wiersz][kolumna] == 1:
                if  plansza2[wiersz][kolumna]== 0.0:
                    kolor=gray1
                    print('pudlo!')
                else:
                    kolor= RED
                    print('WOW TRAFILES')
            else:
                kolor=BLACK


            pygame.draw.rect(screen,kolor,[(przerwy_kratki + szerokosc_plansza) * kolumna + przerwy_kratki,
                                           (przerwy_kratki + wysokosc_plansza) * wiersz + przerwy_kratki,
                                            wysokosc_plansza, wysokosc_plansza])

    # Limit to 60 frames na sekunde
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()




# to i tak nie dziala os.remove("GRACZ_STATKI.npy")
