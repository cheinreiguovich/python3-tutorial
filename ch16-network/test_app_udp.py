#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Test program'

__author__ = 'Charles Guo'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
url, port = '127.0.0.1', 9999
sample = [b'Evan', b'Fred', b'George', b'Hank']
for x in sample:
	s.sendto(x, (url, port))
	print(s.recv(1024).decode('utf-8'))
s.sendto(b'exit', (url, port))
s.close()