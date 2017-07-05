#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Operations of files and directories: Exercise 2'

__author__ = 'Charles Guo'

import os

def searchfile(d, s):
	
	files = []
	
	if not os.path.isdir(d):
		raise TypeError('Input is not a directory!')
		
	if not isinstance(s, str):
		raise TypeError('Input is not a string!')
	
	for x in os.listdir(d):
		abspath = os.path.join(d, x)
		if os.path.isdir(abspath):
			searchfile(abspath, s)
		if os.path.isfile(abspath) and s in os.path.split(abspath)[1]:
			files.append(abspath)
	
	print(files)
	
	
if __name__ == '__main__':
	pwd = os.path.abspath('.')
	searchfile(pwd, '.py')
