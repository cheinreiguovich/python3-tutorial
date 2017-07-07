#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Collections'

__author__ = 'Charles Guo'

from collections import namedtuple

pnt_tuple = namedtuple('Point', ['x', 'y'])    # namedtuple('Name', 'Property')
p = pnt_tuple(1,2)
print('This is a point:\n%s %s %s\n' % (p, p.x, p.y))

clc_tuple = namedtuple('Circle', ['x_c', 'y_c', 'r'])
c = clc_tuple(1,2,3)
print('This is a circle:\n%s %s %s %s\n' % (c, c.x_c, c.y_c, c.r))

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')    # add right element
q.appendleft('y')    # add left element
q.append('z')
q.popleft()    # delete left element
print(q, '\n')

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key_1'] = 'abc'
print(dd['key_1'], dd['any'], '\n')

from collections import OrderedDict
l = [('a',1),('b',2),('c',3)]
print(l)
d = dict(l)
print(d)
od0 = OrderedDict(l)
print(od0)
od = OrderedDict()
od['Fred'] = 30
od['Jack'] = 10
od['Mike'] = 20
print(list(od.keys()))    # Order = adding sequence

class FIFOOrderedDict(OrderedDict):
	
	def __init__(self, capacity):
		super(FIFOOrderedDict, self).__init__()
		self._capacity = capacity
	
	def __setitem__(self, key, val):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print('Remove: ', last)
		if containsKey:
			del self[key]
			print('Set: ', (key, val))
		else:
			print('Add: ', (key, val))
		OrderedDict.__setitem__(self, key, val)
		
from collections import Counter

c = Counter()
for ch in 'asynchron':
	c[ch] = c[ch] + 1
print(c)
