import socket
import threading

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv.bind(('192.168.0.102', 44444))
serv.listen()

clients = []
nicknames = []

def broadcast(text):
    for client in clients:
        client.send(text)



def handle (client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} вышел из чата!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = serv.accept()
        print("Подключение {}".format(str(address)))
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)


        print("Никнейм {}".format(nickname))
        broadcast("{} подключился".format(nickname).encode('utf-8'))
        client.send("Подключен к серверу".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Запуск чата")
receive()



