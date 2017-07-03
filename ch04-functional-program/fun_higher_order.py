# higher order function

fun_name = abs
print(fun_name)

x1 = abs(-10)
print("x1 =",x1)

some_fun = abs
x2 = some_fun(-10)
print("x2 =",x2)

def fun_add(x,y,f):
    return f(x)+f(y)
x3 = fun_add(-5,6,abs)
print("x3 =",x3)

def fun1(x):
    return x ** 2
x4 = map(fun1,range(1,10))
print("x4 =",list(x4))

from functools import reduce
def fun2(x,y):
    return x+y
x5 = reduce(fun2,range(10)[::2])    # 0+2+4+6+8
print("x5 =",x5)

def str2int(s):
    def fxy(x,y):
        return x * 2 + y
    def char2num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    # return reduce(fxy,map(char2num,s))
    return reduce(lambda x,y: x * 2 + y, map(char2num,s))
x6 = str2int('123')
print("x6 =",x6)

def normalize(name):
    return name[0].upper() + name[1:].lower()
x7 = map(normalize, ['adam','LISA','barT'])
print("x7 =",list(x7))

def prod(L):
    return reduce(lambda x,y: x * y, L)
x8 = prod([1,3,5,7])
print("x8 =",x8)

def str2float(s):
    idx_pnt = s.index(".")
    def char2num(s):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
    digit_int = reduce(lambda x,y: x * 10 + y,map(char2num,s[0:idx_pnt]))
    digit_float = reduce(lambda x,y: x * 10 + y,map(char2num,s[idx_pnt+1:]))
    return digit_int + digit_float/(10 ** len(s[idx_pnt+1:]))
x9 = str2float('123.456')
print("x9 =",x9)

def is_odd(x):
    return x % 2 == 1
x10 = filter(is_odd,range(1,10))
print("x10 =", list(x10))

def del_empty(s):
    return s and s.strip()
x11 = filter(del_empty,["a","","B",None,"c"])
print("x11 =",list(x11))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_div_bool(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_div_bool(n),it)

x12 = []
for n in primes():
    if n < 20:
        x12.append(n)
    else:
        break
print("x12 =", x12)

def is_palindrome(n):
    return str(n) == str(n)[::-1]
x13 = filter(is_palindrome,range(10,200))
print("x13 =",list(x13))

x14 = sorted([36,5,-12,9,-21],key=abs)
print("x14 =",list(x14))

x15 = sorted(['bob', 'about', 'dog', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print("x15 =",list(x15))

def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
x16 = sorted(L, key=by_name)
print("x16 =",list(x16))
x17 = sorted(L, key=by_score, reverse=True)
print("x17 =",list(x17))