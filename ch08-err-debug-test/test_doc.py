#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Test documents'

__author__ = 'Charles Guo'

import re

# m = re.search('(?<=abc)def', 'abcdef')
# print(m.group(0))

class Dict(dict):
	'''
	A simple dict class with basic access such as x.y
	
	>>> d1 = Dict()
	>>> d1['x'] = 100
	>>> d1.x
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = Dict(a = 1, b = 2, c = '3')
	>>> d2.c
	'3'
	'''
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)
		
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' has no attribute of '%s'" % (key))
			
	def __setattr__(self, key, val):
		self[key] = val
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
