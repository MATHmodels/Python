from numpy import *
n = 5
x = linspace(0, 4*pi, n+1)
y = x**2*exp(-x/2)*sin(x-pi/3)
print('x =' + ' '.join(['%7.4f'%i for i in x]))
print('y =' + ' '.join(['%7.4f'%i for i in y]))
