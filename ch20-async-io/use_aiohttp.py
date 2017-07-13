#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Use aiohttp'

__author__ = 'Charles Guo'

import asyncio
from aiohttp import web

# Program an HTTP server:
# --- Handle "/" and return '<h1>Index</h1>'
# --- Handle "/hello/{name}" and return '<h1>Hello, %s!</h1>'

async def index(request):
	await asyncio.sleep(0.5)
	text = '<h1>Index</h1>'
	return web.Response(body = text.encode('utf-8'))

async def hello(request):
	await asyncio.sleep(0.5)
	text = '<h1>Hello, %s!</h1>' % (request.match_info['name'])
	return web.Response(body = text.encode('utf-8'))

async def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET', '/', index)
	app.router.add_route('GET', '/hello/{name}', hello)
	host, port = '127.0.0.1', 8000
	srv = await loop.create_server(app.make_handler(), host, port)
	print('Server started at http://%s:%s' % (host, port))
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()