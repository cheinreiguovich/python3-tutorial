# return function

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
x1 = lazy_sum(1,3,5,7,9)
print('x1 =',x1, '\t', x1())

def count1():
    fs = []
    for i in range(1,4):
        def fx():
            return i ** 2
        fs.append(fx)
    return fs
fs1, fs2, fs3 = count1()
print('x2 =', fs1(), '\t', fs2(), '\t', fs3())

def count2():
    fs = []
    def fx(n):
        def gx():
            return n ** 2
        return gx
    for i in range(1,4):
        fs.append(fx(i))
    return fs
fs4, fs5, fs6 = count2()
print('x3 =', fs4(), '\t', fs5(), '\t', fs6())