#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Hashlib'

__author__ = 'Charles Guo'

import hashlib

x1 = hashlib.md5()
x1.update('How to use md5?'.encode('utf-8'))
print(x1.hexdigest())

x2 = hashlib.sha1()
x2.update('How to use sha1 in '.encode('utf-8'))
x2.update('python3-hashlib?'.encode('utf-8'))
print(x2.hexdigest())

def calc_md5(pw):
	pw_md5 = hashlib.md5()
	pw_md5.update(pw.encode('utf-8'))
	return pw_md5.hexdigest()

'''
name    | password
--------+----------
michael | 123456
bob     | abc999
alice   | alice2008

'''
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
	
def login(usr, pw):
	return db[usr] == calc_md5(pw)
	
print(login('bob', 'abc999')) 

def calc_md5_with_salt(pw):
	return calc_md5(pw + 'the-Salt')
	
db = {}

def register(usr, pwd):
	db[usr] = calc_md5(pwd + usr + 'the-Salt')
	
def login(usr, pwd):
	if usr in db:
		return 'Login Successful!' if db[usr] == calc_md5(pwd + usr + 'the-Salt') else 'Login Failed!'
	else:
		raise KeyError('User does not exist!')
    
register('Adam', 'abc123')
register('Bob', 'Def$$$')
register('Carl', 'Ghi12!')
print(login('Bob', 'Def$$$'))
print(login('Carl', 'abc123'))
