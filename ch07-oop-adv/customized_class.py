#!/user/bin/env python3
# -*- coding: utf-8 -*-

'Customized class'

__author__ = 'Charles Guo'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (Name: %s)' % (self.name)

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute of \'%s\'' % (item))

    def __call__(self, *args, **kwargs):
        print('My name is %s' % (self.name))


s = Student('Bob')
s.score = 60
del s.score
print(s)
print(s())
print(s.score)
print(s.age())
# print(s.city)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            idx1 = item.start
            idx2 = item.stop
            if idx1 is None:
                idx1 = 0
            a, b = 0, 1
            L = []
            for x in range(idx2):
                if x >= idx1:  # Save all elements that satisfy the start condition
                    L.append(a)
                a, b = b, a + b
            return L


fib = []
for n in Fib():
    fib.append(n)
print(list(fib))

f = Fib()
print(list(f[3:9]))


class Chain(object):

    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __call__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
print(Chain().status.user('Bob').timeline.list)    # fun(), the parenthese is a symbol of call