import socket



#_______________________________________________________________________
#                 CONNECTING TO SERVER                                  |
#_______________________________________________________________________|
                                                                    #class ktora bedzie laczyc nas z serverem

class Laczenie:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.server='25.67.177.163'
        self.server = 'localhost'
        self.port=9999
        self.addr=(self.server, self.port)
        self.id=self.connect()
        #self.id=self.connect()                                      #musi byc id zyby bylo wiadome, ktory player jest ktory
                                                   # powinno printowac ze polaczono
    #def get_pos(self):
     #   return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    def wysylaj (self, data):                                                            #metoda ktora bedzie wysylane
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e :
            print (e)
n=Laczenie()
print(n.wysylaj('aaaaaaa'))