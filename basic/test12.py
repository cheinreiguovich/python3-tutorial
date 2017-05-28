# Generator

L = [x ** 2 for x in range(10)]    #List
print 'L =',L

G = (x ** 2 for x in range(10))    # Generator
print 'G =',G

for i in G:
    print i
    
# Fibonacci
def Fibnacci(n):
    i, x1, x2 = 0, 0, 1
    L = [];
    return Fib(i,n,x1,x2,L)

def Fib(i,n,x1,x2,L):
    L.append(x2)
    x1, x2 = x2, x1+x2
    i = i+1
    if i < n:
        return Fib(i,n,x1,x2,L)
    else:
        return L

Fib = Fibnacci(5)
print 'Fib =', Fib

def Fib2(n):
    L = []
    i, x1, x2 = 0, 0, 1
    while i < n:
        L.append(x2)
        x1, x2 = x2, x1 + x2
        i = i + 1
    return L

Fib2 = Fib2(5)
print 'Fib2 =', Fib2   