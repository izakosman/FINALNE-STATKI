import pygame
import numpy as np
import random as ran
import sys
import _thread

from TWOJAPLANSZA import TWOJAPLANSZA
from STRZELANIE_W_PRZECIWNIKA import STRZELANIE_W_PRZECIWNIKA

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


def initTwojaPlansza(screen):
    twojaPlansza = TWOJAPLANSZA()
    twojaPlansza.window_gameBoard(screen)

def initPlanszaPrzeciwnika(screen):
    strzelaniePrzeciwnika = STRZELANIE_W_PRZECIWNIKA()
    strzelaniePrzeciwnika.window_gameBoard(screen)

def eventShoot(screen):
    strzelaniePrzeciwnika = STRZELANIE_W_PRZECIWNIKA()
    strzelaniePrzeciwnika.plansza_klikaj(screen)

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
    pygame.display.flip()

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
            pokaz_gre.blit(pygame.transform.scale(plansza, (363, 363)), (520, 86))
            pokaz_gre.blit(pygame.transform.scale(plansza, (363, 363)), (40, 86))
            initTwojaPlansza(pokaz_gre)
            initPlanszaPrzeciwnika(pokaz_gre)
            pokaz_gre.blit(czat,(40,470))
            pokaz_gre.blit(czat2,(40,525))
            pokaz_gre.blit(wyjdz, (430, 730))
            pokaz_gre.blit(text1, text1rect)
            pokaz_gre.blit(text2, text2rect)
            pokaz_gre.blit(text3, text3rect)
            pygame.display.update()
            pokaz_gre.blit(eventShoot(pokaz_gre))



            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

pvp()