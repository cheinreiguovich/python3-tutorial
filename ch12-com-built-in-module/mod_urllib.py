#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'URLlib'

__author__ = 'Charles Guo'

from urllib import request

'''
# Get headers

with request.urlopen('http://www.baidu.com') as f:
	data = f.read()
	print('Status:',f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))
'''

'''
# Disguise with HTTP headers

req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	data = f.read()
	print('Status:',f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))
'''	

from urllib import parse

'''
# Login

print('Login to "Weibo.cn"...')
tele = input('Cellphone: ')
pswd = input('Password: ')
login_data = parse.urlencode([
	('username', tele), 
	('password', pswd), 
	('entry', 'mweibo'), 
	('client_id', ''), 
	('savestate', '1'), 
	('ec', ''),
	('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

'''
# Handler

proxy_handler = request.ProxyHandler({'http':'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
	pass
'''

# Exercise

def fetch_xml(url):
	with request.urlopen(url) as f:
		data = f.read().decode('utf-8')
	print(data)

url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22hangzhou%2C%20china%22)&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
fetch_xml(url)

