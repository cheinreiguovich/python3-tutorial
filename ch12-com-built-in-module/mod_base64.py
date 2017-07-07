#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Base64'

__author__ = 'Charles Guo'

import base64

x1 = base64.b64encode(b'binary\x00string')
print('Encode: %s' % (x1))
x2 = base64.b64decode(x1)
print('Decode: %s' % (x2))


def safe_base64_decode(s):
	return base64.b64decode(s + b'=' * (4 - len(s) % 4))
	
print('Exercise: \n')
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
