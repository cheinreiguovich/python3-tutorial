#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Review 01: TCP Programming'

__author__ = 'Charles'

import socket

# Set a client
tcp_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_conn.bind(('localhost', 9999))

conn = tcp_conn
addr = 'www.baidu.com'
conn.connect((addr, 80))

# Send data
conn.send(('GET /HTTP/1.1\r\nHost: ' + addr + '\r\nConnection: close\r\n\r\n').encode('utf-8'))

# Receive data
buf = []
while True:
	d = conn.recv(512)
	if d:
		buf.append(d)
	else:
		break
data_recv = b''.join(buf)
conn.close()

# Save data
print(len(data_recv))
header, html = data_recv.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('./index.html', 'wb') as f:
	f.write(html)