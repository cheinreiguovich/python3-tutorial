#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Debug'

__author__ = 'Charles Guo'

def fun1(s):
	n = int(s)
	# print('>>> n = %d' % (n))
	assert n != 0, 'n is zero'
	return 10 / n
	
def fun1_main():
	fun1('0')
	
# fun1_main()

import logging
logging.basicConfig(level=logging.INFO)

import pdb
# 'n' = next line
# 'c' = continue
# 'q' = quit
# 'l' = display code
# 'p s' = display variable s

s = '0'
n = int(s)
pdb.set_trace()
# logging.info('n = %d' % (n))
print(10 / n)
