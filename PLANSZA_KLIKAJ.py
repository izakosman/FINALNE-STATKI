import pygame
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






def grid_choose():
                                           #wysokosc i szerokosc planszy
    szerokosc_plansza = 30
    wysokosc_plansza = 30
    przerwy_kratki = 2                     #margines miedzy kazda z komorek planszy

    #__________________________________________________________________________________________________________________
    #                                 STWORZ 2 WYMIAROWY ARRAY                                                         |
    #__________________________________________________________________________________________________________________|

    plansza = []
    for wiersz in range(10):                               # czyli chcemy miec 10 wierszy w naszym array
                                                           # pusty array ktory bedzie mial liste wszystkich koorek dla tego wirsza
        plansza.append([])
        for kolumna in range(10):
            plansza[wiersz].append(0)

    plansza[1][5] = 1                                      #scal kolumne 1 i wiersz 5 do 1 (bo zaczyna sie od 0)

    pygame.init()

    #__________________________________________________________________________________________________________________
    #                                         GLOWNA PETLA                                                             |
    #__________________________________________________________________________________________________________________|


    done=False
    # ________________________________________________________________________POBIERANIE KOORDYNATOW Z PLANSZY
    while not done:
        for event in pygame.event.get():                                         # gdy uzytkownik cos zrobi
            if event.type == pygame.QUIT:                                        # jesli kliknie wyjdz
                done = True                                                      # zaznacz ze skoncz prace

            elif event.type == pygame.MOUSEBUTTONDOWN:                           # gdy uzytkownik kliknie pobierz
                pos = pygame.mouse.get_pos()                                     # koordynaty kursora
                kolumna = pos[0] // (szerokosc_plansza + przerwy_kratki)         # zmien kolumne i y na koordynaty typowe dla planszy
                wiersz = pos[1] // (wysokosc_plansza + przerwy_kratki)           # czyli zamiast 123213,93287437 bedzie np 1 1
                plansza[wiersz][kolumna] = 1                                     # stworz jedna lokacje z wiersza i kolumny
                print("Click ", pos, "koordynaty planszy: ", wiersz, kolumna)



        # ______________________________________________________________________RYSOWANIE PLANSZY
        for wiersz in range(10):
            for kolumna in range(10):
                kolor = gray3
                if plansza[wiersz][kolumna] == 1:
                    kolor = GREEN
                pygame.draw.rect(pokaz_gre, kolor, [(580+30,
                                                    100+30,
                                                 wysokosc_plansza, wysokosc_plansza)])
                                                                                  #tu jest to rysowanie 10 wierszy i kolumn
                                                                                 #pygame.draw.rect(pokaz_gre, kolor,( x gdzie sie ma zaczynac wiersz, y gdzie sie zaczyna kolumna, wysokosc , szerokosc),

                                                                                    # Limit to 60 frames na sekunde
        clock.tick(60)

                                                                                    #update  screen.
        pygame.display.flip()

grid_choose()