#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Getting information from objects'

__author__ = 'Charles Guo'

import types

def fn():
	pass

print(type(123) == int)
print(type('abc') == str)

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)

print(type([x ** 2 for x in range(10)]) == list)
print(type((x ** 3 for x in range(10))) == types.GeneratorType)

print(isinstance('a', str))
print(isinstance(b'a', bytes))
print(isinstance([1,2,3], (list, tuple)))
print(isinstance((1,2,3), (list, tuple)))    # if obj is one of the types

text = 'abc'
print(dir(text))
print(len(text))
print(text.__len__())

class MyDog(object):
	
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))

class MyObj(object):
	
	def __init__(self):
		self.x = 9
	
	def power(self):
		return self.x ** 2

obj = MyObj()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 10)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404))
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())

def readimage(fp):
	if hasattr(fp, 'read'):
		return readdata(fp)
	return None

print(readimage(123))
