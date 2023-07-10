import socket
import threading

addr = ("192.168.0.102", 44444)


nickname = input("Введите никнейм: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def recive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print('Ошибка')
            client.close()
            break
    
def write():
    while True:
        message = '{} :{}'.format(nickname, input(""))
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=recive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

def reg():
    nickname = input('Введите никнейм')
    while True:
        flag = False
        for ex in nickname:
            if nickname == ex:
                flag = True
        if flag == True:
             nickname = input('Данный никнейм уже существует введите новый')
        else: 
            break
        
    password = input('Введите пароль')
    ty_password = input('Повторно введите пароль')
    while True:
        if password == ty_password:
            print("регистрация прошла успешно")
            nicknames.append(nickname)

            break
        else: 
            ty_password = input('Пароль был указан не верно введите его заного')