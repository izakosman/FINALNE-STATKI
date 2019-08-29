

import socket
from _thread import *
import threading
import sys

#server='25.67.177.163'
server='localhost'
port=9999                                                                         #wiele portow i duzo z nich nie jest uzywane dla taich portow jak ten



#    ____________________________________________________________________________________________
#   |                                       SOCKET                                               |
#   |____________________________________________________________________________________________|

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                  # TYPY POLACZEN, JESLI LACZYMY SIE DO IVP4
                                                                                      #bindujemy serwer i port do socketa
try:
    s.bind((server,port))
except socket.error as e:                                                             #jezeli port bedzie zajty to to exceptuemy
    str(e)
                                                                                      # zastawiamy polaczenie
s.listen(2)                                                                           #otwieramy port 2 bo chce, aby tylko 2 ludzi miala mozliwosc sie polaczyc

print('Rozpoczęto pracę serwera. Oczekiwanie na połączenie...')


#    ____________________________________________________________________________________________
#   |                                    Funkcja THREAD                                          |
#   |____________________________________________________________________________________________|



def thr_klient(conn):                                                                   #conn od connection
    conn.send(str.encode('Polaczono... '))
    reply=''
    while True: # chcemy zebyciagle dzialalo w momencie gdy klient jest uruchomiony
        try:
            data= conn.recv(2048)                                                          #watosc informacji ktore chcemy odebrac jesli error to powieksz liczbe i im wieksza tym dluzszy czas na odebranie i przetworzenie
            reply=data.decode('utf-8')                                                  #incode informacja, zeby bylo mozliwe odczytanie

            if not data:
                print('Utracono polaczenie')
                break                                                                   #utrac polaczenie klient
            else:
                print('Odebrano: ', reply)                                                  #czyli odebralismy odpowiedz
                print('Wysylanie: ',reply )
            conn.sendall(str.encode(reply))                                             #encode str reply do bitow
        except:
            break
while True :                                                                            # czyli wszystko ustawimy to wrzucamy do while abu ciagle probowac nawiazac polaczenie
    conn, addr= s.accept()                                                              # akceptuj kazde przychodzace polaczene, magazynuj conn i addr czyli ip addres
    print('polaczono cie  do: ', addr)                                             # kiedy juz znajdzie polaczenie poinformuj o tym

    start_new_thread(thr_klient, (conn, ))
