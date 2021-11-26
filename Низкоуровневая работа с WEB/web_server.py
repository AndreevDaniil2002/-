import socket
from threading import Thread
import os
import time


def create_server():
    with open("settings.txt", "r") as settings:
        for line in settings:
            print(line)
            port = line.split(' ')[1]
            print(port)
            max_value = line.split(' ')[5]
            print(max_value)
            directory = line.split(' ')[3]
            print(directory)
    # Доп задание 2 - файл с общими настройками
    sock = socket.socket()
    try:
        sock.bind(('', int(port)))
    except OSError:
        sock.bind(('', 8080))
    print("Server is on")
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        thread = Thread(target=server_is_on, args=(conn, addr, directory, max_value, ))
        # Доп задание 4 - многопоточность
        thread.start()


def write_log(error, addr, datetime):
    with open('LOG.txt', 'a') as f:
        f.write(str(addr) + ' ')
        f.write(str(datetime) + ' ')
        f.write(error + ' ')
        f.write('\n')


def server_is_on(conn, addr, dir, max_value):
    error = ""
    print("Joined", addr)
    datetime = time.asctime(time.gmtime()).split(' ')
    datetime = f'{datetime[0]}, {datetime[2]} {datetime[1]} {datetime[4]} {datetime[3]}'
    print("Date: ", datetime)
    h = f'HTTP/1.1 200 OK\nServer: SelfMadeServer v0.0.1\nDate: {datetime}\nContent-Type: text/html; charset=utf-8\nConnection: close\n\n'
    os.chdir(dir)
    user = conn.recv(int(max_value)).decode()
    rez = user.split(" ")[1]
    file_format = rez.split('.')[1]
    if file_format == 'html' or file_format == 'css' or file_format == 'js' or file_format == 'ico' or file_format == 'png':
        if rez == '/' or rez == '/index.html':
            with open('index.html', 'rb') as f:
                answer = f.read()
                conn.send(h.encode('utf-8') + answer)
            write_log("", addr, datetime)
        elif rez == "/1.html":
            with open('1.html', 'rb') as f:
                answer = f.read()
                conn.send(h.encode('utf-8') + answer)
            write_log("", addr, datetime)
        elif rez == "/1.png":
            with open("print_img.html", "rb") as f:
                answer = f.read()
                conn.send(h.encode('utf-8') + answer)
            write_log("", addr, datetime)
        else:
            error = "error: 404"
            with open('ERROR_404.html', 'rb') as f:
                answer = f.read()
                conn.send(h.encode('utf-8') + answer)
            write_log(error, addr, datetime)
    else:
        error = "error: 403"
        with open('ERROR_403.html', 'rb') as f:
            answer = f.read()
            conn.send(h.encode('utf-8') + answer)
        write_log(error, addr, datetime)


if __name__ == "__main__":
    create_server()
