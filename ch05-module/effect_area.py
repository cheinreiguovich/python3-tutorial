#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# effect area

def _private_1(text):
	print("Hello, %s" % (text))
def _private_2(text):
	print("Hi, %s" % (text))
def greeting(text):
	if len(text) > 3:
		return _private_1(text)
	else:
		return _private_2(text)

if __name__ == '__main__':
	greeting("abc")
	greeting("abcdefg")

