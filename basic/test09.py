# Iteration

def fun1(x):
    return fun_1(x,1)
def fun_1(n,p):
    if n == 0:
        return p
    return fun_1(n - 1, n * p)

y = fun1(4)
print "y =",y

