import pygame
import sys
import numpy
import os
import numpy as np
import random as ran

from SIEC import SIEC

def sentShoot(data):
    siec = SIEC()
    siec.wysylaj(data)

class STRZELANIE_W_PRZECIWNIKA():
    def window_gameBoard(self, screen):
        planszaprzeciwnika = (np.load('PRZECIWNIK_PLANSZA.npy', mmap_mode='r'))
        RED = (255, 0, 0)

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

        plansza2=[]

        for wieersz in range(10):                                  #czyli chcemy miec 10 wierszy w naszym array
                                                         #pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
            plansza2.append([])
            for kolumnaa in range(10):
                plansza2[wieersz].append(0)

        plansza2[1][5] = 0
        plansza2=planszaprzeciwnika

        for wiersz in range(10):
            for kolumna in range(10):
                pygame.draw.rect(screen, RED,
                    [540 + ((przerwy_kratki + szerokosc_plansza) * kolumna + przerwy_kratki),
                        106 + ((przerwy_kratki + wysokosc_plansza) * wiersz + przerwy_kratki), szerokosc_plansza, wysokosc_plansza])

    def plansza_klikaj(self, screen):
        planszaprzeciwnika = (np.load('PRZECIWNIK_PLANSZA.npy', mmap_mode='r'))
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        gray1=(199,199,199)

        plansza= []

        for wieersz in range(10):                                  #czyli chcemy miec 10 wierszy w naszym array
            #                                              #pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
            plansza.append([])
            for kolumnaa in range(10):
                plansza[wieersz].append(0)

        plansza2=[]

        for wieersz in range(10):                                  #czyli chcemy miec 10 wierszy w naszym array
                                                         #pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
            plansza2.append([])
            for kolumnaa in range(10):
                plansza2[wieersz].append(0)

        plansza2[1][5] = 0
        plansza2=planszaprzeciwnika

        plansza[1][5] = 0                                            ## scal kolumne 1 i wiersz 5 do 1 (bo zaczyna sie od 0)
        szerokosc_plansza = 30
        wysokosc_plansza = 30
        przerwy_kratki = 2

        done = False

        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():  # gdy uzytkownik cos zrobi
                if event.type == pygame.QUIT:  # jesli kliknie wyjdz
                    done = True  # zaznacz ze skoncz prace

                elif event.type == pygame.MOUSEBUTTONDOWN:  # gdy uzytkownik kliknie pobierz
                    pos = pygame.mouse.get_pos()  # koordynaty kursora
                    kolumna = (pos[0] - 540) // (szerokosc_plansza + przerwy_kratki)  # zmien kolumne i y na koordynaty typowe dla planszy
                    wiersz = (pos[1] - 106) // (wysokosc_plansza + przerwy_kratki)  # czyli zamiast 123213,93287437 bedzie np 1 1
                    plansza[wiersz][kolumna] = 1  # stworz jedna lokacje z wiersza i kolumny


                    if plansza[wiersz][kolumna] == 1:
                        if plansza2[wiersz][kolumna] == 0.0:
                            kolor = gray1
                            print('pudlo!')
                        else:
                            kolor = GREEN
                            print('WOW TRAFILES')
                    else:
                        kolor = RED

                    pygame.draw.rect(screen, kolor, [540 + ((przerwy_kratki + szerokosc_plansza) * kolumna + przerwy_kratki), 106 + ((przerwy_kratki + wysokosc_plansza) * wiersz + przerwy_kratki), szerokosc_plansza, wysokosc_plansza])

                    pygame.display.flip()

                    sentShoot([wiersz, kolumna])

        clock.tick(60)

        # update  screen
        pygame.display.flip()