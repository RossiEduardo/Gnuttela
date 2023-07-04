# Especificação do trabalho

## Objetivo
Compreender conceitos relacionados à Sistemas distribuidos.

### Linguagens em que o trabalho pode ser realizado
C, C++ e C#, python,

## Definição do Trabalho
Neste trabalho pretende-se que o aluno implemente um sistema distribuido visto em sala,
podenso ser um sitema de arquivo distribuido, um protoloco de comunicação distribuido
como o torrent, etc, ou seja sistema que envolve os conceitos discutidos e apresentados em
sala de aula. Sejam criativos.

## O que deve ser entregue
- Descritivo o grupo deverá entregar o descritivo do trabalho indicando qual
será o sistema e em que partes serão tratados os elementos solicitados.
Nome completo e número USP de todos os integrantes do trabalho.
- A entrega será via e-disciplinas.
- O código o endereço de onde estar o código na qual foi
implementado
- O sistema pode ser desenvolvido em qualquer uma das linguagens
especficadas, desde que sejam entregues todas as bibliotecas
necessárias para sua execução.
- Deverá ser entregue um manual, demonstrando como instalar e como
executar o sistema . Neste manual devem estar descritas as partes de
implementação, sendo explicadas o porque e como foram utilizadas.
- Entrega da apresentação do trabalho final deve ser explicados no
código fonte do projeto os pontos de implementação e executando
um caso de uso.

## Avaliação
Serão considerados para avaliação:
- Relatorio e implementaçao (65%);
- Apresentação (45%);

## Membros

| Nome                           | nUSP     |
|--------------------------------|----------|
| Adrio Oliveira Alves           | 11796830 |
| Eduardo Vinicius Barbosa Rossi | 10716887 |
| João Victor Sene Araújo        | 11796382 |
| Thiago Henrique Cardoso        | 11796594 |
| Victor Paulo Cruz Lutes        | 11795512 |

# Implementação

## Objetivo

Desenvolvimento de um Chat Peer-to-Peer Distribuído com Servidor de Visualização de Clientes Conectados, de modo que o sistema a ser projetado possa proporcionar uma comunicação direta e segura entre os usuários, sem a necessidade de um intermediário centralizado, ou seja, fazer um projeto que imite, de certa forma, as funcionalidades do software cliente Gnutella, impletementado em Python3 utilizando a biblioteca Twisted.

## Manual e Funcionalidades

- server.py: Servidor
- client.py: Cliente

É necessário ter Python 3 instalado em sua máquina, bem como instalar a biblioteca. Para instalar a biblioteca via terminal, utilize a seguinte linha de comando:

```console
$ pip install twisted
```

Após instalar as dependências, podemos executar o projeto. Assim, podemos abrir os servidores:

```console
$ python3 server.py
```

Após isso, será solicitado uma entrada de porta. Neste projeto, vamos colocar as portas 8000, 8001 e 8002, isto é, serão criados apenas 3 servidores (para facilitar o projeto), já que o cliente escolherá, dentre essas 3 portas, qual se conectar.

Depois de abrir os 3 servidores, podemos, então, executar os arquivos dos clientes com o seguinte comando:

```console
$ python3 client.py
```

Assim, o cliente irá se conectar em algum servidor, sendo possível ver qual servidor o cliente se conectou através dos terminais dos servidores (através de uma mensagem de $READY$ que o cliente envia ao servidor escolhido).

Desse modo, é exibido na tela desse único cliente que não há outros usuários online. Então, se adicionarmos mais usuários, poderemos visualizar novamente a lista no terminal do usuário, vendo os novos clientes adicionados (para adicionar novos clientes, basta repetir os passos anteriores, onde o primeiro cliente foi iniciado).

Nesse sentido, será solicitado que o cliente insira o host (ip) do cliente no qual ele deseja se conectar, pedindo a porta do cliente alvo logo em seguida. Nisso, quando os dois clientes entrarem com as informações um do outro, eles estarão conectados em uma conexão peer-to-peer, sem a necessidade dos servidores. Agora, eles poderão enviar mensagens de texto um para o outro via entrada no terminal.

Nesse ponto, o usuário pode sair do chat digitando $EXIT$ (no campo da mensagem), saindo do campo P2P e voltando para a parte principal, onde poderá visualizar os usuários conectados na rede. Seguindo essa linha, se o usuário digitar $QUIT$ no campo do host, ele irá finalizar o programa, saindo da lista de usuários online.

## Apresentação

[![Vídeo de Apresentação](https://img.youtube.com/vi/SoLleqpqE2w/0.jpg)](https://www.youtube.com/watch?v=SoLleqpqE2w)