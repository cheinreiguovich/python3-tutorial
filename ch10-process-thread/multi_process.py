#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Multiprocessing'

__author__ = 'Charles Guo'

import os

'''
print('Process (%s) starts...' % (os.getpid()))
pid = os.fork()
if pid == 0:
	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''

from multiprocessing import Process

'''
def run_proc(name):
	print('Run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s. ' % (os.getpid()))
	p = Process(target = run_proc, args = ('test',))
	print('Child process will start...')
	p.start()
	p.join()
	print('Child process ends.')
'''

from multiprocessing import Pool
import time, random

'''
def big_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	st = time.time()
	time.sleep(random.random() * 3)
	et = time.time()
	print('The task %s runs %0.2f s. ' % (name, (et-st)))
	
if __name__ == '__main__':
	print('Parent process %s. ' % (os.getpid()))
	p = Pool(4)
	for i in range(4):
		p.apply_async(big_task, args = (i,))
	print('Waiting for all sub-processes done...')
	p.close()
	p.join()
	print('All sub-processes are done')
'''

import subprocess

'''
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
'''

'''
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
'''

from multiprocessing import Queue

def write(q):
	print('Process to write: %s' % (os.getpid()))
	for val in ['A', 'B', 'C']:
		print('Put %s to queue...' % (val))
		q.put(val)
		time.sleep(random.random())

def read(q):
	print('Process to read: %s' % (os.getpid()))
	while True:
		val = q.get(True)
		print('Get %s from queue. ' % (val))

if __name__ == '__main__':
	q = Queue()
	pw = Process(target = write, args = (q,))
	pr = Process(target = read, args = (q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()

