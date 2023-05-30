from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()

    # O server receve o datagrama do cliente
    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode("utf-8")
        # se o server recebe o ready do nosso cliente, todos os outros clientes sao adicionados em addresses
        if datagram == "ready":
            addresses = "\n".join([str(x) for x in self.clients])

            # os outros clientes serao enviados para o nosso cliente
            self.transport.write(addresses.encode('utf-8'),addr)
            self.clients.add(addr)


if __name__ == '__main__':
    reactor.listenUDP(9999, Server())
    reactor.run()