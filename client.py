from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint
import time

class Client(DatagramProtocol):
    def __init__(self, host, port):
        if host == 'localhost':
            host = '127.0.0.1'

        self.id = host, port
        self.address = None
        self.server = '127.0.0.1',9999
        print("Working on id:",self.id)

    # Quando o cliente eh iniciado, startamos o nosso protocolo e dizemos pro server que o cliente
    #esta "ready"
    def startProtocol(self):
        self.transport.write("ready".encode("utf-8"), self.server)

    # O cliente recebe o datagram do server com todos os outros clientes
    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode('utf-8')
       
        # o cliente deve escolher um server para se conectar
        if addr == self.server:
            if(len(datagram) == 0 or datagram == str(self.id)):
                print("No one is online")
                print("Press any key to search again:")
                input()
                print("Searching...")
                time.sleep(2)
                reactor.callInThread(self.startProtocol)
            else:
                print(f"(You: {self.id}) Choose a client from these:\n{datagram}")
                self.address = input("Write host:"),int(input("Write port:"))
                reactor.callInThread(self.send_message)
        else:
            print(addr, ":", datagram)
    
    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.address)

if __name__ == '__main__':
    port = randint(1000,5000) #esse random eh necessario para que nao tenhamos dois clientes numa mesma porta
    reactor.listenUDP(port, Client('localhost',port))
    reactor.run()