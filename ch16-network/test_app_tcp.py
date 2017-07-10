#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Test program'

__author__ = 'Charles Guo'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url, port = '127.0.0.1', 9999
s.connect((url, port))
print(s.recv(1024).decode('utf-8'))
sample = [b'Adam', b'Bob', b'Carl', b'Dave']
for x in sample:
	s.send(x)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()