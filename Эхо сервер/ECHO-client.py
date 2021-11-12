import socket
from time import sleep
from threading import Thread


def check():
	while True:
		try:
			data = sock.recv(1024)
			msg = data.decode()
			print(msg)
		except:
			break


try:
	sock = socket.socket()
	x = input('Введите хост: ')
	y = int(input('Введите порт: '))
	sock.connect((x, y))
except:
	x = 'localhost'
	y = 9091
	y = 9095
	sock.connect((x, y))

msg = ''

passwd = input('Введите пароль: ')
msg = passwd
sock.send(msg.encode())

Thread(target=check).start()

while msg !="close":
	msg = input()
	if msg !='close':
		sock.send(msg.encode())




msg = 'client disconnected'
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()