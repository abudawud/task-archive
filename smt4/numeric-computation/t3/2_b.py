import numpy as np
from math import exp

print("x f(x) tanda")
print("---------------")

beda = 0.10
i = 1
tanda = {}
for x in np.arange(0, 1.1, beda):
    f = exp(-x) - x
    print("%3.1f %6.3f" %(x, f), end=' ')
    
    if f < 0:
        tanda[i] = '-'
        print(tanda[i])
    else:
        if f > 0:
            tanda[i] = '+'
            print(tanda[i])
        else:
            tanda[i] = '0'
            print(tanda[i])
    i += 1

i = 1
for x in np.arange(0, 1.1, beda):
    if tanda[i] == '0':
        print("Akarnya adalah = %6.4f" %(x))
    else:
        if i > 1:
            if tanda[i] != tanda[i-1]:
                a = x - beda
                b = x
                print("\nAkar ada di interval [%3.1f, %3.1f]" %(a, b))
    i += 1