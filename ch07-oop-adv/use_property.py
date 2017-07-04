#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Use @property'

__author__ = 'Charles Guo'

class Student(object):
	
	def get_score(self):
		return self._score
	
	def set_score(self, val):
		if not isinstance(val, int):
			raise ValueError('The score has to be an Integer!')
		elif val < 0 or val > 100:
			raise ValueError('The score has to be between 0 ~ 100!')
		self._score = val

s = Student()
s.set_score(60)
print(s.get_score())

class Student(object):
	
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, val):
		if not isinstance(val, int):
			raise ValueError('The score has to be an Integer!')
		elif val < 0 or val > 100:
			raise ValueError('The score has to be between 0 ~ 100!')
		self._score = val

s = Student()
s.score = 60
print(s.score)

class Student(object):
	
	@property
	def birthyear(self):
		return self._birthyear
		
	@birthyear.setter
	def birthyear(self, val):    # The attribute of birthyear is r/w
		self._birthyear = val
	
	@property
	def age(self):    # The attribute of age is r only
		return 2017 - self._birthyear
		
class Screen(object):
	
	@property
	def width(self):
		return self._wdith
		
	@width.setter
	def width(self, val):
		self._width = val
		
	@property
	def height(self):
		return self._height
		
	@height.setter
	def height(self, val):
		self._height = val
		
	@property
	def resolution(self): 
		return self._width * self._height
		
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
	
	
