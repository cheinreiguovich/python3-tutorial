#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Using __slots__'

__author__ = 'Charles Guo'

class Student(object):
	pass

s = Student()
s.name = 'Michael'
print(s.name)

s2 = Student()

def setage(self, age):
	self.age = age

from types import MethodType
s.setage = MethodType(setage, s)    # Bind a method to a instance
s.setage(25)
print(s.age)

def setscore(self, score):
	self.score = score
Student.setscore = setscore    # Bind a method to a class
s.setscore(100)

s2.setscore(50)
print(s.score)
print(s2.score)

class Student(object):
	__slots__ = ('name', 'age')    # use tuple to bind attributes
	
s = Student()
s.name = 'Michael'
s.age = 25
print(hasattr(s, 'name'))
print(hasattr(s, 'age'))


class GradStu(Student):
	pass

g = GradStu()
g.name = 'Adam'
g.score = 99
print(hasattr(g, 'name'))
print(hasattr(g, 'score'))

