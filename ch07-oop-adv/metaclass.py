#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Metaclass'

__author__ = 'Charles Guo'

class Hello(object):

    def hello(self, name = 'world'):
        print('Hello, %s' % (name))

def fn(self, name = 'world'):
    print('Hello, %s' % (name))

Hello1 = type('Hello', (object,), dict(hello=fn))
h = Hello1()
h.hello()
print(type(Hello1))
print(type(h))

class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L1 = MyList()
L2 = list()
for i in range(10):
    L1.add(i)
    L2.append(i)
print(L1)
print(L2)

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % (name))
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute of '%s'" % (key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'Please insert %s (%s) values (%s)' % (self.__table__, ','.join(fields,), ','.join(params))
        print('SQL: %s' % (sql))
        print('ARGS: %s' % (str(args)))

class User(Model):

    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id = 12345, name = 'Bob', email = 'bob@orm.org', password = 'my-pwd')
u.save()