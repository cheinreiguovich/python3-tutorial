# Parameters
# order: normal, default, changable/named, kw

# 1. normal parameter
def fun_1(a,b):
    # power function
    y = a ** b
    return y

y1 = fun_1(2,3)
print "y1 =",y1

# 2. default parameter
def fun_2(a,b = 2):
    # power function
    y = a ** b
    return y

y2 = fun_2(2,7)
print "y2 =",y2

# 3. changable parameter
def fun_3(*num):
    # sum of squares
    y = 0
    for i in num:
        y = y + i * i
    return y

y3 = fun_3(1,2,3)    # deal with elements with *; deal with arr without *
print "y3 =",y3

# 4. key word parameter
def fun_4(name,age,**kw):
    # enrollment system
    print 'name:',name,'age:',age,'other:',kw
    
fun_4('Adam',6,city = 'BJ')    # to display kw, the name of kw must be given


# 5. named key word parameter
def fun_5(name, age, *, city = 'BJ', job):
    # enrollment system
    print name,age,city,job

fun_5('Bob',30,job = 'Engineer')