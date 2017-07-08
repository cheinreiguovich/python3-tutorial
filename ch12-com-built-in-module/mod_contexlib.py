#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Contexlib'

__author__ = 'Charles Guo'

'''
# Use of 'with'
class Query(object):
	
	def __init__(self, name):
		self.name = name
	
	def __enter__(self):
		print('Begin')
		return self
	
	def __exit__(self, exc_type, exc_val, traceback):
		if exc_type:
			print('Error')
		else:
			print('End')
			
	def query(self):
		print('Query info about %s...' % (self.name))
		
with Query('Bob') as q:
	q.query()
'''

from contextlib import contextmanager as ctmgr
class Query(object):
	
	def __init__(self, name):
		self.name = name
	
	def query(self):
		print('Query info about %s...' % (self.name))
		
print()
@ctmgr
def new_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

with new_query('Bob') as q:
	q.query()

print()
@ctmgr
def tag(name):
	print('<%s>' % (name))
	yield
	print('</%s>' % (name))

with tag('text_1'):
	print('hello')
	print('world')


from contextlib import closing
from urllib.request import urlopen


print()
@ctmgr
def closing(s):
	try:
		yield s
	finally:
		s.close()
with closing(urlopen('https://www.python.org')) as p:
	for line in p:
		print(line)

