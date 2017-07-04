#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Inheritance and Polymorphism'

__author__ = 'Charles Guo'

class Animal(object):
	
	def __init__(self):
		pass
		
	def run(self):
		print('The Animal is running')
		
class Dog(Animal):
	
	def run(self):
		print('The Dog is running')
		
	def eat(self):
		print('The Dog eats meat')
		
class Cat(Animal):
	
	def run(self):
		print('The Cat is running')
		
	def eat(self):
		print('The Cat eats fish')
		
class Tortoise(Animal):
	
	def run(self):
		print('The Tortoise is running slowly...')

def runtwice(someanimal):
	someanimal.run()
	someanimal.run()

animal = Animal()

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
cat.eat()

print('Is dog an instance of Dog?', isinstance(dog, Dog))
print('Is dog an instance of Animal?', isinstance(dog, Animal))

runtwice(animal)
runtwice(dog)
runtwice(cat)
runtwice(Tortoise())
