from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

import time

class ServerProtocol(DatagramProtocol):
    def __init__ (self):
        self.allClients = set()
        self.servers = set()


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
        if datagram == "READY":
            print("\tREADY from", addr)

            # adiciona o cliente "inicial" na "base de dados"
            insertText = "INSERT_CLIENTS_DATA " + str(addr)
            self.transport.write(insertText.encode("utf-8"), ("228.0.0.1", 9999))

            # send message to distributed servers
            self.transport.write(b"REQUEST_CLIENTS_DATA", ("228.0.0.1", 9999))

            reactor.callInThread(self.awserClient, addr)
            
            
        # response contaning the clients    
        elif datagram.startswith('RESPONSE_CLIENTS_DATA'):
            response = datagram[22:]
            address_list = response.split("\n")
            
            self.allClients.update(address_list)
            
            # print(self.allClients)

    def awserClient(self, addr):
        # waits all servers responses
        time.sleep(2)

        response = "\n".join(str(item) for item in self.allClients)

        # returns to first client
        self.transport.write(response.encode("utf-8"), addr)



# Actualy a handler for multicast 
class DistributedServerProtocol(DatagramProtocol):
    def __init__ (self):
        self.myClients = set() 
        self.myServers = set()   
    
    def startProtocol(self):
        self.transport.joinGroup('228.0.0.1')

    def datagramReceived(self, datagram, address):
        datagram = datagram.decode("utf-8")

        if datagram == 'REQUEST_CLIENTS_DATA':
            # Process the request for client data
            client_data = self.collect_client_data()

            # Send the client data response back to the main server
            self.transport.write(client_data.encode("utf-8"), address)

        elif datagram.startswith('INSERT_CLIENTS_DATA'):
            datagram = datagram[20:]

            self.myClients.add(eval(datagram))

            print("distributed clients: ",self.myClients)


    def collect_client_data(self):
        # Perform the necessary logic to gather the client data
        # Return the client data as a string
        # header:
        client_data = "RESPONSE_CLIENTS_DATA\n"
        # content: (myclients stringified)
        client_data += "\n".join([str(x) for x in self.myClients])

        return client_data

# We use listenMultiple=True so that we can run MulticastServer.py and
# MulticastClient.py on same machine:

port = int( input ("PORTA: ") )

reactor.listenMulticast(port, ServerProtocol(), listenMultiple=True)

reactor.listenMulticast(9999, DistributedServerProtocol(), listenMultiple=True)

reactor.run()