#!usr/bin/env python3
# -*- coding: utf-8 -*-

'Read files'

__author__ = 'Charles Guo'

'''
try:
	f = open('./test_1.txt', 'r')
	print(f.read())
finally:
	if f:
		f.close()
'''

print('\nOpening file 1:')
with open('./test_1.txt', 'r') as f:
	# print(f.read())
	# print(f.read(10))
	for line in f.readlines():
		print(line.strip())    # Delete the ending '\n' in all lines

print('\nOpening file 2:')
with open('./test_1.txt', 'rb') as f:
	print(f.read())
	
print('\nOpening file 3:')
with open('./test_2.txt', 'r', encoding = 'gbk', errors = 'ignore') as f:
	print(f.read())
	
print('\nWriting file 4:')
with open('./test_3.txt', 'w') as f:
	f.write('Hello, world!')
	
print('\nWriting file 5:')
with open('./test_4.txt', 'w', encoding = 'gbk') as f:
	f.write('你好')
