#!/usr/bin/env python3
# -*- coding:: utf-8 -*-

'Web Server Gateway Interface'

__author__ = 'Charles Guo'

from wsgiref.simple_server import make_server
#from hello import application

def application(env, start_resp):
	start_resp('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (env['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
