#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Itertools'

__author__ = 'Charles Guo'

import itertools

'''
# count()
c1 = itertools.count(1)
for n in c1:
	print(n)
'''

'''
# cycle()
c2 = itertools.cycle('abc')
for n in c2:
	print(n)
'''

'''
# repeat()
c3 = itertools.repeat('x',3)
for n in c3:
	print(n)
'''

'''
# takewhile()
c4 = itertools.count(1)
c4s = itertools.takewhile(lambda x: x <= 10, c4)
print(list(c4s))
'''

'''
# chain()
c5 = itertools.chain('abc', 'XYZ')
for n in c5:
	print(n)
'''

# groupby()
c6 = itertools.groupby('aaabbbccaaa')
for key, gp in c6:
	print(key, list(gp))

c7 = itertools.groupby('AaaBBbcCAAa', lambda c: c.upper())
for key, gp in c7:
	print(key, list(gp))

