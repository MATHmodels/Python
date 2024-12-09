import math
x = 1.2; N = 25; k = 1; s = x; sign = 1.0

while k < N:
    sign = -sign
    k = k + 2
    term = sign*x**k/math.factorial(k)
    s = s + term
    
print('sin(%g) = %g (%d 项近似值)' % (x, s, N))
