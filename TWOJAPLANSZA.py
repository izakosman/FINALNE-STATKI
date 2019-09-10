import pygame
import sys
import numpy
import os
import numpy as np
import random as ran

screenGlob = None
twojestatki = (np.load('GRACZ_STATKI.npy', mmap_mode='r'))
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (0, 0, 0)

szerokosc_plansza = 30
wysokosc_plansza = 30
przerwy_kratki = 2

class TWOJAPLANSZA():
    def window_gameBoard(self, screen):
        global screenGlob
        screenGlob = screen

        plansza = []
        for wiersz in range(10):  # czyli chcemy miec 10 wierszy w naszym array # pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
            plansza.append([])
            for kolumna in range(10):
                plansza[wiersz].append(0)

        plansza[1][5] = 0  ## scal kolumne 1 i wiersz 5 do 1 (bo zaczyna sie od 0)
        plansza = twojestatki

        clock = pygame.time.Clock()

        for wiersz in range(10):
            for kolumna in range(10):
                kolor = RED
                if plansza[wiersz][kolumna] != 0:
                    kolor = GREEN

                pygame.draw.rect(screenGlob, kolor, [60 + ((przerwy_kratki + szerokosc_plansza) * kolumna + przerwy_kratki), 106 + ((przerwy_kratki + wysokosc_plansza) * wiersz + przerwy_kratki), szerokosc_plansza, wysokosc_plansza])

            clock.tick(60)

        return;

    def reciveShoot(self, screen, kolumna, wiersz):
        pygame.draw.rect(screen, WHITE, [60 + ((przerwy_kratki + szerokosc_plansza) * kolumna + przerwy_kratki),
                                         106 + ((przerwy_kratki + wysokosc_plansza) * wiersz + przerwy_kratki),
                                         szerokosc_plansza, wysokosc_plansza])
        pygame.display.flip()