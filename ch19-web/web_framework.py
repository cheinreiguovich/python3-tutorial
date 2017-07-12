#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Web Framework'

__author__ = 'Charles Guo'

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods = ['GET'])
def signin_form():
	return '''<form action = '/signin' method = 'post'>
			  <p><input name = 'usnm'></p>
			  <p><input name = 'pswd'></p>
			  <p><button type = 'submit'>Sign in</button></p>
			  </form>'''
@app.route('/signin', methods = ['POST'])
def signin():
	if request.form['usnm'] == 'admin' and request.form['pswd'] == 'admin':
		return '<h3>Hello, Admin!</h3>'
	return '<h3>Username or password is not correct!</h3>'
	
if __name__ == '__main__':
	app.run()
