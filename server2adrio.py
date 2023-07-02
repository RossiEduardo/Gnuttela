from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ServerProtocol(DatagramProtocol):
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
        
    
    # O server receve o datagrama do cliente
    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode("utf-8")
        # se o server recebe o ready do nosso cliente, todos os outros clientes sao adicionados em addresses
        if datagram == "ready":
            # send message to distributed servers
            self.transport.write(b"REQUEST_CLIENTS_DATA", ("228.0.0.1", 9999))
            
            
        # response contaning the clients    
        elif datagram.startswith('RESPONSE_CLIENTS_DATA'):
            response = datagram[22:]
            # address_list = datagram.split("\n")
            
            # self.allClients.update(address_list)
            
            # print(self.allClients)
            print(response)
            
 
# Actualy a handler for multicast 
class DistributedServerProtocol(DatagramProtocol):
    def __init__ (self):
        return
    
    
    def startProtocol(self):
        self.transport.joinGroup('228.0.0.1')

    def datagramReceived(self, datagram, address):
        if datagram == b'REQUEST_CLIENTS_DATA':
            # Process the request for client data
            client_data = self.collect_client_data()
            
            print(address)

            # Send the client data response back to the main server
            self.transport.write(client_data.encode("utf-8"), address)

    def collect_client_data(self):
        # Perform the necessary logic to gather the client data
        # Return the client data as a string
        client_data = "RESPONSE_CLIENTS_DATA\nClient 2"

        return client_data

# We use listenMultiple=True so that we can run MulticastServer.py and
# MulticastClient.py on same machine:
reactor.listenMulticast(8899, ServerProtocol(), listenMultiple=True)

reactor.listenMulticast(9999, DistributedServerProtocol(), listenMultiple=True)

reactor.run()