#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Pickling'

__author__ = 'Charles Guo'

import pickle

d = dict(name = 'Bob', age = 20, score = 88)
with open('./dump.txt', 'wb') as f:
	pickle.dump(d, f)
with open('./dump.txt', 'rb') as f:
	print('Python-pickle:', pickle.load(f))
	
import json
print('JSON:', json.dumps(d))    # Python to JSON
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print('JSON-anti-pickle:', json.loads(json_str))    # JSON to Python

class Student(object):
	
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
	
def stu2dict(stu):
	return {
		'name': stu.name,
		'age': stu.age,
		'score': stu.score
	}

def dict2stu(d):
	return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)
print(json.dumps(s, default = stu2dict))
print(json.dumps(s, default = lambda obj: obj.__dict__))
print(json.loads(json_str, object_hook=dict2stu))
