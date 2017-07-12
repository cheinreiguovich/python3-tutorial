#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Use templates: Model-View-Controller (MVC)'

__author__ = 'Charles Guo'

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/signin', methods = ['GET'])
def signin_form():
	return render_template('form.html')
	
@app.route('/signin', methods = ['POST'])
def signin():
	acc = request.form['usnm']
	pwd = request.form['pswd']
	if acc == 'admin' and pwd == 'admin':
		return render_template('signin-ok.html', username = acc)
	elif pwd == '123456':
		return render_template('signin-ok.html', username = acc)
	return render_template('form.html', message = 'Username or password is incorrect!', username = acc)

if __name__ == '__main__':
	app.run()
