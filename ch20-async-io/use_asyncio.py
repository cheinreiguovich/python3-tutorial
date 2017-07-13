#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Use asyncio'

__author__ = 'Charles Guo'

import asyncio, threading

@asyncio.coroutine
def hello():
	print('Hello world! (%s)' % (threading.currentThread()))
	yield from asyncio.sleep(1)
	print('Hello again! (%s)' % (threading.currentThread()))

@asyncio.coroutine
def wget(host):
	print('wget %s...' % (host))
	conn = asyncio.open_connection(host, 80)
	reader, writer = yield from conn
	header = 'GET /HTTP/1.0\r\nHost: %s\r\n\r\n' % (host)
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		line = yield from reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	writer.close()    # Ignore body and close socket

	
loop = asyncio.get_event_loop()
#tasks = [hello(), hello()]
tasks = [wget(host) for host in ['www.google.com', 'www.facebook.com', 'www.yahoo.com', ]]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

