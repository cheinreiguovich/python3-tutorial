# Customed abs()

def customed_abs(x):
    if x >= 0:
        return x
    else:
        return -x

a = -10
abs_a = customed_abs(a)
print "abs of a is",abs_a