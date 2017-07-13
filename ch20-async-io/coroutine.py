#/usr/bin/env python3
# -*- coding: utf-8 -*-

'Coroutine'

__author__ = 'Charles Guo'

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % (n))
		r = '200 OK'
		
def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n += 1
		print('[PRODUCER] Producing %s...' % (n))
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' % (r))
	c.close()

c = consumer()
produce(c)	

'''
def test():
	for x in range(10)[2:8:2]:
		yield x
	return
a = test()
print(a.send(None))
print(a.send(1))
print(a.send(2))
'''