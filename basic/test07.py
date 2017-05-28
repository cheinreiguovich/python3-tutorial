# Roots of quadratic function
# ax^2 + bx + c = 0
import math

a = 1
b = 3
c = 2

def quadratic(a,b,c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        print "Real solution"
        delta = math.sqrt(d)
        x1 = (-b + delta) / (2 * a)
        x2 = (-b - delta) / (2 * a)
        mark = 1
        x = (x1,x2,mark)
        return x
    else:
        print "Complex solution"
        d = -d
        delta = math.sqrt(d)
        real = -b / 2
        imag = delta/2
        mark = 2
        x = (real,imag,mark)
        return x
    

r = quadratic(a,b,c)
if r[-1] == 1:
    print "Solution:",r[0],'\t\t',r[1]
elif r[-1] == 2:
    print "Solution:",r[0],'+',r[1],'i','\t\t',r[0],'-',r[1],'i'