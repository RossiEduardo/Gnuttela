from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

serversConnectPort = 8888

class MulticastPingPong(DatagramProtocol):
    def __init__ (self):
        self.myClients = set()
        self.allClients = set()
        self.servers = set()
        
        self.myClients.add("adrIP")
        self.myClients.add("testIP")


    def startProtocol(self):
        # Called after protocol has started listening.
        # Set the TTL>1 so multicast will cross router hops:
        self.transport.setTTL(5)
        # Join a specific multicast group:
        self.transport.joinGroup("228.0.0.1")

        # todos os server receberão (incluindo nos mesmos - pois estamos no grupo)
        # self.transport.write(b"Connect servers", ("228.0.0.5", serversConnectPort)
    '''
    def datagramReceived(self, datagram, address):
        print("Datagram %s received from %s" % (repr(datagram), repr(address)))
        if datagram == b"Client: Ping" or datagram == "Client: Ping":
            # Rather than replying to the group multicast address, we send the
            # reply directly (unicast) to the originating port:
            self.transport.write(b"Server: Pong", address)
    '''
    
    # O server receve o datagrama do cliente
    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode("utf-8")
        # se o server recebe o ready do nosso cliente, todos os outros clientes sao adicionados em addresses
        if datagram == "ready":
            print("aAa")
            # send message to distributed servers
            self.transport.write(b"REQUEST CLIENTS", ("228.0.0.1", serversConnectPort))
            '''
            addresses = "\n".join([str(x) for x in self.clients])

            # os outros clientes serao enviados para o nosso cliente
            self.transport.write(addresses.encode('utf-8'),addr)
            self.clients.add(addr)
            '''
            
        # datagram from other server in the group requesting my clients
        elif datagram == "REQUEST CLIENTS":
            print("bBb")
            addresses = "\n".join([str(x) for x in self.myClients])

            # return datagram contening addresses list to the server that requests
            self.transport.write(addresses.encode('utf-8'), addr)
            
        # response contaning the clients    
        else:
            print("cCc")
            address_list = datagram.split("\n")
            # print(address_list)
            # address_list= ["novoIP", "abcIP"]
            
            self.allClients.update(address_list)
            
            print(self.allClients)
            
            
    
    def responseRecived(self, responses):
        print("cccc")
        for x in responses:
            print(x)
        

# We use listenMultiple=True so that we can run MulticastServer.py and
# MulticastClient.py on same machine:
reactor.listenMulticast(8888, MulticastPingPong(), listenMultiple=True)
reactor.run()