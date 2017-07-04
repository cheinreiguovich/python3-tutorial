#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Errors'

__author__ = 'Charles Guo'

def foo():
	r = some_func()
	if r == (-1):
		return (-1)
	return r

def bar():
	r = foo()
	if r == (-1):
		print('Error')
	else:
		print('Pass')

'''
try:
	print('Try...')
	# r = 10/0
	# r = 10/int('a')
	r = 10/int('2')
	print('Result: ', r)
except ZeroDivisionError as e:
	print('Zero Division Error:', e)
except ValueError as e:
	print('Value Error:', e)
else:
	print('No Error!')
finally: 
	print('Finally...')
print('End')
'''

'''
try:
	foo()
except ValueError as e:
	print('Value Error!')
except UnicodeError as e:	# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
	print('Unicode Error!')
'''

import logging

def fun1(s):
	return 10/int(s)
def fun2(s):
	return fun1(s) * 2
def fun3():
	try:
		print('Try...')
		fun2('0')
	except Exception as e:
		logging.exception(e)
	finally:
		print('Finally...')
# print('End!')
# fun3()

class FooError(ValueError):
	pass

def fun4(s):
	n = int(s)
	if n == 0:
		raise FooError('Invalid value: %s' % (s))
	return 10 / n
# fun4('0')

def fun5():
	try:
		fun4('0')
	except ValueError as e:
		print('Value Error!')
		raise
# fun5()

'''
try:
	10 / 0
except ZeroDivisionError:
	raise ValueError('Input Error!')
'''	
	
n = 1
if n > 0:
	raise ValueError

