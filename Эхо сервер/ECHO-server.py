import socket
sock = socket.socket()
import random
connected_users = []


while True:
	try:
		port = 9090
		sock.bind(('', port))
		break
	except:
		port = random.randint(1024,65535)
		sock.bind(('', port))

sock.listen(0)
print("Использую порт: ", port)

msg = ''
while True:
	conn, addr = sock.accept()
	connected_users.append(conn)
	strok = str(addr[0])
	passwd0 = conn.recv(128)
	s = 'N'.encode()
	passwd = str(passwd0.decode()) + '\n'
	with open('addresses.txt', 'r', encoding='utf-8') as file:
		for line in file:
			line1 = line.split(';')
			if strok == line1[0] and passwd == line1[1]:
				print("Приветствую", addr[0], '!')
				break
		else:
			send_msg = 'Вы новый пользователь? Y/N'
			conn.send(send_msg.encode())
			s = conn.recv(1024)
			if s.decode() == 'N':
				conn.send('Неверный пароль'.encode())
	if s.decode() == 'Y':
		with open('addresses.txt', 'a', encoding='utf-8') as file:
			file.write(str(addr[0]) + ';' + str(passwd))
	with open('server_log.txt', 'a', encoding='utf-8') as file:
		file.write(str(addr) + '  ' + 'connected\n')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
		if msg != 'client disconnected':
			print(addr, msg)
			for user in connected_users:
				if conn != user:
					temp = str(addr) + str(msg)
					user.send(temp.encode())
		else:
			with open('server_log.txt', 'a', encoding='utf-8') as file:
				file.write(str(addr) + '  ' + 'disconnected\n')
				try:
					connected_users.remove(conn)
				except:
					break
	conn.close()