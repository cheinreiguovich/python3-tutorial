#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Operation of files and directories'

__author__ = 'Charles Guo'

import os

# Basic info
print(os.name,'\n')
print(os.uname(),'\n')
print(os.environ,'\n')
print(os.environ.get('PATH'),'\n')
print(os.environ.get('x', r"This is 'x'"),'\n')

# Files and directories
print(os.path.abspath('.'))
print(os.path.join('.', 'testdir'))
os.mkdir('./testdir')
os.rmdir('./testdir')
print(os.path.split('./file_dir_op.py'))
print(os.path.splitext('./file_dir_op.py'))
with open('./test.txt', 'w') as f:
	f.write('testing...')
os.rename('test.txt', 'test.py')
os.remove('test.py')

# Copy files
#import shutil
#copyfile()

# List all
print([x for x in os.listdir('.')])

# List directories
print([x for x in os.listdir('.') if os.path.isdir(x)])

# List files with certain ext
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# Exercise 1
from datetime import datetime

pwd = os.path.abspath('.')

print('Simulated Operation: dir -l')
for x in os.listdir(pwd):
	fsize = os.path.getsize(x)
	mtime = datetime.fromtimestamp(os.path.getmtime(x)).strftime('%Y-%m-%d %H:%M')
	flag = '/' if os.path.isdir(x) else ''
	print('%10d  %s  %s%s' % (fsize, mtime, x, flag))

