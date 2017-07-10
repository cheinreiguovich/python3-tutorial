#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Sample GUI program'

__author__ = 'Charles Guo'

from tkinter import *
import tkinter.messagebox as msgbox

class Application(Frame):
	
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel = Label(self, text = 'Hello, world!')
		self.helloLabel.pack()
		self.quitButton = Button(self, text = 'Quit', command = self.quit)
		self.quitButton.pack()
		self.textInput = Entry(self)
		self.textInput.pack()
		self.alertButton = Button(self, text = 'Hello', command = self.hello)
		self.alertButton.pack()
	
	def hello(self):
		text = self.textInput.get() or 'world'
		msgbox.showinfo('Message: Hello, %s' % (text))
		
someapp = Application()
someapp.master.title('First GUI')
someapp.mainloop()
