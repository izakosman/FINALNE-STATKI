import pygame
import sys
import numpy
import os
import numpy as np
import random as ran


class TWOJAPLANSZA():
    def window_gameBoard(self, screen):
        twojestatki = (np.load('GRACZ_STATKI.npy', mmap_mode='r'))
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        gray1 = (199, 199, 199)
        gray2 = (232, 232, 232)
        gray3 = (220, 220, 220)

        #_______________________________________________________wysokosc i szerokosc planszy
        szerokosc_plansza = 30
        wysokosc_plansza = 30

        #_______________________________________________________margines miedzy kazda z komorek planszy
        przerwy_kratki = 2

        plansza = []

        for wiersz in range(10):  # czyli chcemy miec 10 wierszy w naszym array
            # pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
            plansza.append([])
            for kolumna in range(10):
                plansza[wiersz].append(0)

        plansza[1][5] = 0  ## scal kolumne 1 i wiersz 5 do 1 (bo zaczyna sie od 0)
        plansza = twojestatki

        clock = pygame.time.Clock()

        # __________________________________________________________________________________________
        #                             GLOWNA PETLA                                                 |
        # __________________________________________________________________________________________|
        #while not done:
            #for event in pygame.event.get():  # gdy uzytkownik cos zrobi
                #if event.type == pygame.QUIT:  # jesli kliknie wyjdz
                    #done = True  # zaznacz ze skoncz prace
                    #quit()

        for wiersz in range(10):
            for kolumna in range(10):
                kolor = RED
                if plansza[wiersz][kolumna] != 0:
                    kolor = GREEN
                pygame.draw.rect(screen, kolor,
                    [60 + ((przerwy_kratki + szerokosc_plansza) * kolumna + przerwy_kratki),
                        106 + ((przerwy_kratki + wysokosc_plansza) * wiersz + przerwy_kratki), szerokosc_plansza, wysokosc_plansza])

            # Limit to 60 frames na sekunde
            clock.tick(60)

        return;

'''        twojestatki = (np.load('GRACZ_STATKI.npy', mmap_mode='r'))

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
        plansza=twojestatki

        #__________________________________________________________________________________________
        #                                                OKNO                                      |
        #__________________________________________________________________________________________|
        # szerokosc i wysokosc okienka

        WINDOW_SIZE = [323, 323]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        # nazwa okna
        pygame.display.set_caption("TWOJA PLANSZA")
        # petla do momentu klikniecia
        done = False

        clock = pygame.time.Clock()

        #__________________________________________________________________________________________
        #                             GLOWNA PETLA                                                 |
        #__________________________________________________________________________________________|
        while not done:
            for event in pygame.event.get():                                    # gdy uzytkownik cos zrobi
                if event.type == pygame.QUIT:                                   # jesli kliknie wyjdz
                    done = True                                                 # zaznacz ze skoncz prace
                    quit()

            screen.fill(gray3)

            for wiersz in range(10):
                for kolumna in range(10):
                    kolor = BLACK
                    if plansza[wiersz][kolumna] != 0:
                        kolor = GREEN
                        pygame.draw.rect(screen,kolor,[(przerwy_kratki + szerokosc_plansza) * kolumna + przerwy_kratki,(przerwy_kratki + wysokosc_plansza) * wiersz + przerwy_kratki, wysokosc_plansza, wysokosc_plansza])

            # Limit to 60 frames na sekunde
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()'''
