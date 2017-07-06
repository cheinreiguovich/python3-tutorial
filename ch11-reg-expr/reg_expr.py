#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Regular Expressions'

__author__ = 'Charles Guo'

'''
Basic:
\d = 1 digit
\w = 1 word
\s = 1 space
\- = 1 dash
. = 1 any symbol
* = n any symbols
+ = 1 or more any symbols
? = 0 or 1 any symbol
("?" < "+" < "." < "*")
{n} = n any symbols
{n,m} = n ~ m any symbols
'''

'''
Examples:
\d{3} = 3 digits
\s+ = 1 or more spaces
\d{3,8} = 3 ~ 8 digits

\d{3}\s+\d{3,8}
eg: "010 12345678"

\d{3}\-\d{3,8}
eg: "010-12345678"
'''

'''
Advanced
[] = range

[0-9a-zA-Z\_] = 1 digit/word/underline

[0-9a-zA-Z\_]+ = 1 or more ...
eg: "a100", "0_Z", "Py3000"

[a-zA-Z\_][0-9a-ZA-Z\_]* = 1 word/underline + n digits/words/underlines

[a-zA-Z\_][0-9a-ZA-Z\_]{0,19} = 1 word/underline + 0 ~ 19 digits/words/underlines

A|B = A or B
(P|p)ython = Python or python

^ = start a line
^\d = start with a digit

$ = end a line
\d$ = end with a digit
'''


s = 'ABC\\-001'    # 'ABC-001'
s = r'ABC\-001'    # 'ABC-001'


import re

'''
x1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print('Matching result of x1:', x1)
x2 = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
print('Matching result of x2:', x2)
'''

'''
# Example

reg_str = '^\(\d{3}\)\s?\-\s?\d{3}\s?\d{4}$'
usr_str = '(248)-460 1700'
if re.match(reg_str, usr_str):
	print('Matched!')
else:
	print('Failed!')
'''

'''
# Split

str1 = 'a b   c'
print(str1.split(' '))
print(re.split(r'\s+', str1))
str2 = 'a,b;; c...d'
print(re.split(r'[\s\,\;\.]+', str2))
'''

'''
# Group

() = group
group(0) = origin string
group(i) = i-th sub-string
groups() = all sub-strings

g1 = r'^(\d{3})-(\d{3,8})$'
m = re.match(g1, '010-12345')
print('%s\n%s\n%s' % (m.group(0), m.group(1), m.group(2)))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

print(re.match(r'^(\d+)(0*)$', '102300').groups())    # Greedy matching
print(re.match(r'^(\d+?)(0*)$', '102300').groups())    # Non-greedy matching
'''

'''
# Compile

re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_tel.match('010-12345').groups())
print(re_tel.match('010-1234').groups())
'''

# Exercise I
em_1 = 'someone@gmail.com'
em_2 = 'bill.gates@microsoft.com'
re_ex_1 = re.compile(r'^([\w\.]*)(\@\w*)(.com)$')
print(re_ex_1.match(em_1))
print(re_ex_1.match(em_2))

# Exercise II
em_3 = '<Tom Paris> tom@voyager.org'
# em_3 = 'tom@voyager.org'
re_ex_2 = re.compile(r'^(\<[\w\s\.]*\>\s)?([\w\.]*)(\@\w*)(\.\w{3})$')
gp = list(re_ex_2.match(em_3).groups())
if gp[0] == None:
	gp[0] = '<>'
else: 
	gp[0] = gp[0].strip()
print(gp)
