#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Class and Instance'

__author__ = 'Charles Guo'

class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def printout(self):
		print("%s %s" % (self.name, self.score))
		
	def getgrade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'
	
bart = Student('Bart Simpson', 59)
print('Info of bart:', bart)
print('Info of Student():', Student)
print('Name of Bart:', bart.name)
print('Score of Bart:', bart.score)
print('Grade of Bart:', bart.getgrade())
