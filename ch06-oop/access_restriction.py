#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Access restriction'

__author__ = 'Charles Guo'

class Student(object):
	
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	
	def printout(self):
		print('%s %s' % (self.__name, self.__score))
		
	def getname(self):
		return self.__name
	
	def getscore(self):
		return self.__score
		
	def setscore(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('Bad Score!')
		
bart = Student('Bart Simpson', 59)
# print(bart.__name) is not accessible
print('Access name of Bart:', bart._Student__name)
bart.__name = 'new name'
print('Test new name:', bart.__name)
print('Check Bart name:', bart.getname())

