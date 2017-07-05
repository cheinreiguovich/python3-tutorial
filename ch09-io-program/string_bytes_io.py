#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'StringIO and BytesIO'

__author__ = 'Charles Guo'

from io import StringIO, BytesIO

'''
f = StringIO()
print(f.write('Hello'))
print(f.write(' '))
print(f.write('World!'))
print(f.getvalue())
'''

'''
f = StringIO('Hello World!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
'''

'''
f = BytesIO()
some_txt = f.write('中文'.encode('utf-8'))
print(some_txt)
print(f.getvalue())
'''

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
