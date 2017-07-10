#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Server prgramming'

__author__ = 'Charles Guo'

import socket
import time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Create a socket based on IPv4/TCP
url, port = '127.0.0.1', 9999
s.bind((url, port))    # Bind url and port
s.listen(5)    # Max number = 5
print('Waiting for connections...')

def tcplink(sock, addr):
	print('Accept a new connection from %s: %s' % (addr))
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		send_txt = 'Hello, %s!' % (data.decode('utf-8'))
		sock.send(send_txt.encode('utf-8'))
	sock.close()
	print('The connection from %s: %s is closed.' % (addr))

while True:
	sock, addr = s.accept()    # Accept a new connections
	t = threading.Thread(target = tcplink, args = (sock, addr))    # Create a new thread to handle connections
	t.start()
	t.join()

