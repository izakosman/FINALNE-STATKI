import socket



#_______________________________________________________________________
#                 CONNECTING TO SERVER                                  |
#_______________________________________________________________________|
                                                                    #class ktora bedzie laczyc nas z serverem

class Laczenie:
    def __init__(self):
        self.klient=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server='25.67.177.163'
        self.port=9999
        self.addr=(self.server, self.port)
        self.id=self.connect()
        #self.id=self.connect()                                      #musi byc id zyby bylo wiadome, ktory player jest ktory
        print(self.id)                                              # powinno printowac ze polaczono


    def connect(self):
        try:
            self.klient.connect(self.addr)
            return self.klient.recv(2048).decode()
        except:
            pass
    def

n=Laczenie()