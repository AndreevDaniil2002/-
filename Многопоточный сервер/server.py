import socket, threading
import sys


def accept_client():
    while True:
        cli_sock, cli_add = ser_sock.accept()
        CONNECTION_LIST.append(cli_sock)
        thread_client = threading.Thread(target=broadcast_usr, args=[cli_sock, cli_add])
        thread_client.start()


def broadcast_usr(cli_sock, cli_add):
    with open("identyty.txt", "a") as f_ident:
        f_ident.write(cli_add[0] + " ")
        f_ident.write(str(cli_add[1]) + '\n')
    flag_log = False
    flag_clear_log = False
    flag_ident = False
    while True:
        msg_to_do = input('Введите что вы хотите сделать: ')
        if msg_to_do == 'show logs':
            flag_log = True
        elif msg_to_do == 'clear logs':
            flag_clear_log = True
        elif msg_to_do == 'clear identyty':
            flag_ident = True
        try:
            data = cli_sock.recv(1024)
            with open("log.txt", "a") as f_log:
                f_log.write(str(data.decode()))
                f_log.write('\n')
            if flag_log:
                print(data.decode()+'\n')
            if flag_clear_log:
                with open("log.txt", 'w') as f_log:
                    f_log.write("")
                flag_log = False
            if flag_ident:
                with open ("identyty.txt", "w") as f_ident:
                    f_ident.write("")
                    flag_ident = False
            if data:
                b_usr(cli_sock, data)
        except Exception as x:
            print(x.message)
            break


def b_usr(cs_sock, msg):
    for client in CONNECTION_LIST:
        if client != cs_sock:
            client.send(msg)


if __name__ == "__main__":
    CONNECTION_LIST = []

    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = 'localhost'
    PORT = 7777
    ser_sock.bind((HOST, PORT))

    ser_sock.listen(1)
    print('Chat server started on port : ' + str(PORT))
    thread_ac = threading.Thread(target=accept_client)
    thread_ac.start()