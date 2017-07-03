# anonymous function

x1 = map(lambda x: x ** 2, range(1, 10))
print('x1 =', list(x1))

x2 = lambda x: x ** 3
print('x2 =', x2)


def some_func(x, y):
    return lambda: x ** 2 + y ** 2


x3 = some_func(1, 2)
print('x3 =', x3, '\t', x3())


def some_func():
    return lambda x, y: x ** 2 + y ** 2


x4 = some_func()
print('x4 =', x4, '\t', x4(3, 4))
