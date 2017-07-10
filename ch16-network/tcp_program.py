#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'TCP programming'

__author__ = 'Charles Guo'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url, port = 'www.google.com', 80
s.connect((url, port))

req = b'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnecton: close\r\n\r\n'
s.send(req)

buf = []
while True:
	d = s.recv(1024)
	if d:
		buf.append(d)
	else:
		break
data = b''.join(buf)
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('google.html', 'wb') as f:
	f.write(html)
