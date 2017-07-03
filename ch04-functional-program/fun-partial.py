# partial function

def int2(x, base=2):
    return int(x, base)
x1 = int2('1000')
print('x1 =', x1)

import functools
int2_partial = functools.partial(int, base=2)
x2 = int2_partial('1000')
print('x2 =', x2)
