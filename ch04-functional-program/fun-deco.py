# decorator

def log(func):
    def wrapper(*args, **kw):
        print('Call %s:' % func.__name__)
        return func(*args, **kw)
    return wrapper


def now1():
    print('Test 1\n')
x1 = log(now1)
x1()


@log
def now2():
    print('Test 2\n')
x2 = now2
x2()


def log_1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log_1('Excute')
def now3():
    print("Test 3\n")
x3 = now3
x3()


x4 = log_1("Execute")(now1)
x4()


import functools

def log_2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def log_ex_1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text,str):
                tmp = text
            else:
                tmp = ""
            print("Begin call: %s %s" % (tmp, func.__name__))
            func(*args, **kw)
            print("End call: %s %s" % (tmp, func.__name__))
            return func
        return wrapper
    return decorator


def ex():
    print("abcde")
ex1 = log_ex_1("Execute")(ex)
ex1()