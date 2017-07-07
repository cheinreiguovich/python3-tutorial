#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Struct'

__author__ = 'Charles Guo'

import struct

'''
> = big-endian
I = 4 bytes unsigned int
H = 2 bytes unsigned int
'''
x1 = struct.pack('>I', 10240099)
print(x1)
x2 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(x2)
x3 = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'    # Example: heading 30 chars of a BMP file
x4 = struct.unpack('<ccIIIIIIHH', x3)
print(x4)

def checkBMP(s):
	x = struct.unpack('<ccIIIIIIHH', s)
	if x[0] + x[1] == b'BM':
		print('Size: %s x %s\nColor: %s' % (x[6],x[7],x[len(x)-1]))
	else:
		raise TypeError('This is not a BMP file!')

with open('./testBMP.bmp', 'rb') as f:
	checkBMP(f.read(30))
