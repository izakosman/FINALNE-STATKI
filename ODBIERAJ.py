import json

class ODBIERAJ():
    def odbieraj(self, conn):
        conn.send(str.encode('Polaczono... '))
        while True:  # chcemy zebyciagle dzialalo w momencie gdy klient jest uruchomiony
            try:
                data = conn.recv(2048)
                if not data:
                    print('Utracono polaczenie')
                    break  # utrac polaczenie klient
                else:
                    print('Odebrano: ', json.loads(data.decode()))  # czyli odebralismy odpowiedz
                    print('Wysylanie: ', json.loads(data.decode()))

                    return json.loads(data.decode())
            except:
                break

        return 'Error'