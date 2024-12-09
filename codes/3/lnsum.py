def L(x, n):
    s = 0
    for i in range(1, n+1):
        s += 1/i * (x/(1+x))**i
    return s
    
from math import log as ln
x = 5
print(L(x, 10))
print(L(x, 100))
print(ln(1+x))
