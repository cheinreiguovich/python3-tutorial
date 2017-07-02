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