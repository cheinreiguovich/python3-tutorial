#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Use async/await'

__author__ = 'Charles Guo'

import asyncio, threading

async def hello():
	print('Hello (%s)' % (threading.currentThread()))
	await asyncio.sleep(1)
	print('Hello again!')

async def wget(host):
	print('wget %s...' % (host))
	conn = asyncio.open_connection(host, 80)
	reader, writer = await conn
	header = 'GET /HTTP/1.0\r\nHost: %s\r\n\r\n' % (host)
	writer.write(header.encode('utf-8'))
	await writer.drain()
	while True:
		line = await reader.readline()
		if line == b'\r\n':
			break
		print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
	writer.close()
	
loop = asyncio.get_event_loop()
#tasks = [hello(), hello()]
tasks = [wget(host) for host in ['www.google.com', 'www.youtube.com', 'www.facebook.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()