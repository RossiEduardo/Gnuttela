from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Server(DatagramProtocol):
    def __init__(self):
        self.clients = set()
        self.servers = set()

    def startProtocol(self):
        # Inicie a descoberta de outros servidores
        self.transport.write("discovery".encode('utf-8'), ('255.255.255.255', 9999))

    def datagramReceived(self, datagram, addr):
        datagram = datagram.decode("utf-8")

        if addr not in self.clients and addr not in self.servers:
            # Se o datagrama for uma mensagem de descoberta, adiciona o endereço à lista de servidores
            if datagram == "discovery":
                self.servers.add(addr)
            else:
                # Senão, é um novo cliente
                self.clients.add(addr)

        # Processa os datagramas recebidos
        self.processDatagram(datagram, addr)

    def processDatagram(self, datagram, addr):
        if datagram == "ready":
            # Envia a lista de servidores para o cliente
            server_list = "\n".join([str(x) for x in self.servers])
            self.transport.write(server_list.encode('utf-8'), addr)

            # Adiciona o cliente à lista de clientes
            self.clients.add(addr)

            # Notifica outros servidores sobre o novo cliente
            for server in self.servers:
                self.transport.write("new_client".encode('utf-8'), server)

        elif datagram == "new_client":
            # Adiciona o servidor à lista de servidores
            self.servers.add(addr)

            # Envia a lista de servidores atualizada para todos os clientes
            server_list = "\n".join([str(x) for x in self.servers])
            for client in self.clients:
                self.transport.write(server_list.encode('utf-8'), client)


def main():
    server_port = 9999  # Porta do servidor

    # Inicia o servidor
    reactor.listenUDP(server_port, Server())
    reactor.run()

if __name__ == '__main__':
    main()
