# Array generator

# Array
def fun1(L):
    A = []
    for x in L:
        A.append(2 * x)
    return A
    
Arr = range(2,10)
A = fun1(Arr)
print 'A =',A

B = [2 * x for x in Arr]
print 'B =',B

C = [2 * x for x in Arr if x % 2 == 0]
print 'C =',C

# Permutation
D = [i + j for i in 'XYZ' for j in 'UVW']
print 'D =',D

# OS
def fun2():
    import os
    A = [d for d in os.listdir('.')]
    return A

E = fun2()
print 'E =',E

# Dict
Dic = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, value in Dic.items():
    print key, '=', value

# Practice
L = ['Hello','world',18,'Apple',None]
F = [k.lower() for k in L if isinstance(k,str)]
print 'F =',F