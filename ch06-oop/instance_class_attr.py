#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Attributes of instances and classes'

__author__ = 'Charles Guo'

class Student(object):

	def __init__(self, name):
		self.name = name
		
s = Student('Bob')
s.score = 90

class Student(object):
	
	name = 'Student'
	
s = Student()
print(s.name)
print(Student.name)
s.name = 'Bob'
print(s.name)
print(Student.name)
del s.name
print(s.name)

