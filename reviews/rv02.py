#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Review 02: Inheritance'

__author__ = 'Charles Guo'

from types import MethodType

class Person():
	
	def __init__(self, name, sex, age):
		self._name = name
		self._sex = sex
		self._age = age
		
	def __str__(self):
		return self._name
	
class Student(Person):
	
	def __init__(self, id, name, sex, age, city):
		super(Student, self).__init__(name, sex, age)
		self._id = id
		self._city = city
	
	def __str__(self):
		return '%s: %s' % (self._id, super(Student, self).__str__()) 
		
adam = Person('Adam', 'M', 20)
bob = Student('S-002', 'Bob', 'M', 30, 'Peking')
print(adam)
print(bob)