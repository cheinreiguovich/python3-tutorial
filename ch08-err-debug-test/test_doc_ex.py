#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Exercise of doctest'

__author__ = 'Charles Guo'

def fact(n):
	'''
	
	A function that calculates factorials
	
	Example:
	
	>>> fact(1)
	1
	>>> fact(4)
	24
    
	'''
	if n < 0:
		raise ValueError()
	if n == 0:
		return 1
	if n < 1:
		raise ValueError()
	if n == 1:
		return 1
	return n * fact(n - 1)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
