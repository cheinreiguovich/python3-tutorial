#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'OOP introduction'

__author__ = 'Charles Guo'

class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def printout(self):
		print('%s %s' % (self.name, self.score))
		
if __name__ == '__main__':
	stu1 = Student('Bart Simpson', 59)
	stu2 = Student('Lisa Simpson', 87)
	stu1.printout()
	stu2.printout()

