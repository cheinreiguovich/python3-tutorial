# partial function

def int2(x, base=2):
    return int(x, base)
x1 = int2('1000')
print('x1 =', x1)

import functools
int2_partial = functools.partial(int, base=2)
x2 = int2_partial('1000')
print('x2 =', x2)

kw1 = {'base':2}
x3 = int('10100', **kw1)
print('x3 =', x3)

f4_max2 = functools.partial(max,10)
x4 = f4_max2(5,6,7)
print("x4 =", x4)
