import pygame
import numpy as np
import random as ran
import sys


# INTERFEJS____________________________________________
pygame.init()


#USTAWIENIE WIELKOSCI GLOWNEGO OKNA, ustawilam ako zmiennezebylatwiej mi  bylo pozniej  tym manipulowac
pokaz_gre_szerokosc = 800
pokaz_gre_wysokosc=600


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

# okienko
pokaz_gre=pygame.display.set_mode((pokaz_gre_szerokosc,pokaz_gre_wysokosc))
pygame.display.set_caption("Gra  w statki - I.Kosman")
clock = pygame.time.Clock()

# MUZYKA..........................................................................
pygame.mixer.music.load('muzyczka2.mp3')
pygame.mixer.music.play(-1)

#OBRAZY........................................................................
statek2=pygame.image.load('obrazintro2.png')
statek3=pygame.image.load('obrazintro3.png')
statek4=pygame.image.load('obrazintro4.png')
statek5=pygame.image.load('obrazintro5.png')

statek=[pygame.image.load('obrazintro2.png'),pygame.image.load('obrazintro3.png'),pygame.image.load('obrazintro4.png'),pygame.image.load('obrazintro4.png')]


soundon=pygame.image.load('soundon.png')
soundoff=pygame.image.load('soundoff.png')

nowagra=pygame.image.load('nowagra.png')
nowagra2=pygame.image.load('nowagra2.png')
instrukcja=pygame.image.load('instrukcja.png')
instrukcja2=pygame.image.load('instrukcja2.png')
wyjdz=pygame.image.load('wyjdz.png')
pvp=pygame.image.load('PVP.png')
SOLO=pygame.image.load('SOLO.png')
wyjdz2=pygame.image.load('wyjdz2.png')
pvp2=pygame.image.load('PVP2.png')
SOLO2=pygame.image.load('SOLO2.png')
tlomenu = pygame.image.load('tlomenu.png')

################################################################################################################
#RYSOWANIE TEKSTU_______________________________________________________________________________________________
myfont = pygame.font.SysFont("Comic Sans MS", 30)
label = myfont.render("Python and Pygame are Fun!", 1, black)

######################################################################################################
#gra pvp___________________________________________________________________________________________________________________________________________ pvp




######################################################################################################
#game menu_____________________________________________________________________________________________

def gamemenu():
    # wypelnienie tlo intro
    tlo = pygame.Surface(pokaz_gre.get_size())
    tlo = tlo.convert()
    tlo.fill(white3)

    # blit czyliwszyskoscalamy
    pokaz_gre.blit(tlo, (0, 0))
    pygame.display.flip()###

    #tlomenu = pygame.image.load('tlomenu.png')
    #pokaz_gre.blit(tlomenu, (10, 10))
    gamemen = True
    # MENU............................................................................
    while gamemen:
        pokaz_gre.fill(white3)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse=pygame.mouse.get_pos()
        klik=pygame.mouse.get_pressed()
        pokaz_gre.blit(statek[0], (60, 70))

        if 300 + 100 > mouse[0] > 300 and 300 + 50 > mouse[1] > 299:
            pokaz_gre.blit(pvp2, (300, 300))
            pokaz_gre.blit(SOLO, (300, 370))
            pokaz_gre.blit(wyjdz, (300, 440))
            if klik[0] == 1:
                print('wybrales nowa pvp')
                import PVP

        elif 300 + 100 > mouse[0] > 300 and 370 + 54 > mouse[1] > 369:
            pokaz_gre.blit(SOLO2, (300, 370))
            pokaz_gre.blit(pvp, (300, 300))
            pokaz_gre.blit(wyjdz, (300, 440))
            if klik[0] == 1:
                print('wybrales solowe')

        elif 300 + 100> mouse[0] > 300 and 440 + 54 > mouse[1] > 440:
            pokaz_gre.blit(pvp, (300, 300))
            pokaz_gre.blit(SOLO, (300, 370))
            pokaz_gre.blit(wyjdz2, (300, 440))
            if klik[0]==1:
                gra_intro()
        else:
            pokaz_gre.blit(pvp, (300, 300))
            pokaz_gre.blit(SOLO, (300, 370))
            pokaz_gre.blit(wyjdz, (300, 440))

        pygame.display.update()
        clock.tick(20)


#######################################################################################################
#INSTRUKCJA __________________________________________________________________________________________

def instruction():
    # wypelnienie tlo intro
    tlo = pygame.Surface(pokaz_gre.get_size())
    tlo = tlo.convert()
    tlo.fill(white3)
    # blit czyliwszyskoscalamy
    pokaz_gre.blit(tlo, (0, 0))
    pygame.display.flip()###
    #tlomenu = pygame.image.load('tlomenu.png')
    #pokaz_gre.blit(tlomenu, (10, 10))
    intr = True


    # MENU............................................................................
    while intr:
        pokaz_gre.fill(white3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
        mouse=pygame.mouse.get_pos()
        klik=pygame.mouse.get_pressed()

        if 300+200 > mouse [0] >300 and 515+54>mouse[1]>515:
            pokaz_gre.blit(tlomenu, (60, 40))
            pokaz_gre.blit(instrukcja, (300, 20))
            pokaz_gre.blit(wyjdz2, (300, 515))
            if klik[0] == 1:
                gra_intro()
        else:
            pokaz_gre.blit(tlomenu, (60, 40))
            pokaz_gre.blit(instrukcja, (300, 20))
            pokaz_gre.blit(wyjdz, (300, 515))
        pygame.display.update()
        clock.tick(20)






#####################################################################################################################################
#  GRA MENU __________________________________________________________________________________________________________________
def gra_intro():#to  samomozna zrobic dla pauzy
    # wypelnienie tlo intro
    tlo = pygame.Surface(pokaz_gre.get_size())
    tlo = tlo.convert()
    tlo.fill(white3)
    # blit czyliwszyskoscalamy
    pokaz_gre.blit(tlo, (0, 0))
    pygame.display.flip()
    intro=True
    #MENU............................................................................
    while intro:
        pokaz_gre.fill(white3)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit

        #GUZIKI .....................................................................
        #MYSZ POLOZENIE I KLIKI.......................................................
        #interakcja guzika
        mouse=pygame.mouse.get_pos()
        #print(mouse)
        klik=pygame.mouse.get_pressed()
        #print(klik)
        pokaz_gre.blit(statek[0], (60, 70))

# ZMIANA KOLOROW I PRZEJSCIE Z INTRO DO INNYCH CZESCI
        if 300+200>mouse[0]>300 and 300+50>mouse[1]>299:
            pokaz_gre.blit(nowagra2, (300, 300))
            pokaz_gre.blit(instrukcja, (300, 370))
            pokaz_gre.blit(wyjdz, (300, 440))
            if klik[0]==1:
                gamemenu()
                print('wybrales nowa gre')
        elif 300+200 > mouse [0] >300 and 370+54>mouse[1]>369:
            pokaz_gre.blit(instrukcja2, (300, 370))
            pokaz_gre.blit(nowagra, (300, 300))
            pokaz_gre.blit(wyjdz, (300, 440))
            if klik[0]==1:
                instruction()
                print('wybrales instrukcje')
        elif 300+200>mouse[0]>300 and 440+54>mouse[1]>440:
            pokaz_gre.blit(nowagra, (300, 300))
            pokaz_gre.blit(instrukcja, (300, 370))
            pokaz_gre.blit(wyjdz2, (300, 440))
            print('wyszedles z gry')
        else:
            pokaz_gre.blit(nowagra, (300, 300))
            pokaz_gre.blit(instrukcja, (300, 370))
            pokaz_gre.blit(wyjdz, (300, 440))
        if 710+50 > mouse[0] >690 and  60+50 > mouse[1] >59:
            pokaz_gre.blit(soundoff, (710, 60))
            if klik[0]==1:
                pygame.mixer.music.stop()
        else:
            pokaz_gre.blit(soundon, (710, 60))
        pygame.display.update()
        clock.tick(20)


gra_intro()
pygame.quit()
quit

