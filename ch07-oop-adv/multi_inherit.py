#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Multi-inheritance'

__author__ = 'Charles Guo'

class Animal(object):
	pass

# Top type
class Mammal(Animal):
	pass
	
class Bird(Animal):
	pass
	
# Animaml type
class Dog(Mammal):
	pass

class Bat(Mammal):
	pass
	
class Parrot(Bird):
	pass
	
class Ostrich(Bird):
	pass

# Funcional features
class RunnableMixIn(object):
	def run(self):
		print('Running...')

class FlyableMixIn(object):
	def fly(self):
		print('Flying...')

class CarnivorousMixIn(object):
	def eat(self):
		print('Eat meat')

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
	pass

class Bat(Mammal, FlyableMixIn):
	pass

'''
class MyTCPSrv(TCPSrv, ForkingMixIn):
	pass
	
class MyUDPSrv(UDPSrv, ThreadingMixIn):
	pass

class MyTCPSrv(TCPSrv, CoroutineMixIn):
	pass
'''
