#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Test unit'

__author__ = 'Charles Guo'

class Dict(dict):
	
	def __init__(self, **kw):
		super(Dict, self).__init__(**kw)
	
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute of '%s'" % (key))
	
	def __setattr__(self, key, val):
		self[key] = val
		
# d = Dict(a = 1, b = 2)
# print(d['a'])

import unittest

class TestDict(unittest.TestCase):
	
	def test_init(self):
		d = Dict(a = 1, b = 'test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))
		
	def test_key(self):
		d = Dict()
		d['key'] = 'val'
		self.assertEqual(d.key, 'val')
		
	def test_attr(self):
		d = Dict()
		d.key = 'val'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'val')
		
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
			
	def setUp(self):
		print('setUp...')
	
	def tearDown(self):
		print('tearDown...')
			
if __name__ == '__main__':
	unittest.main()
