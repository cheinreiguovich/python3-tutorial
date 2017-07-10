#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'UDP programming'

__author__ = 'Charles Guo'

import socket as sk
import time

s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)    # DGRAM does not require listen()
s.bind(('127.0.0.1', 9999))

print('Bind UDP on port: 9999...\nWaiting for connections...')
while True:
	data, addr = s.recvfrom(1024)
	time.sleep(1)
	if not data or data.decode('utf-8') == 'exit':
			break
	print('Received from %s: %s' % (addr))
	s.sendto(('Hello, %s!' % (data.decode('utf-8'))).encode('utf-8'), addr)
	
