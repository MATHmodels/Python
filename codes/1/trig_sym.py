from sympy import *
x, y = symbols('x y')
f = -sin(x)*sin(y) + cos(x)*cos(y)
print('f =',f)

simplify(f)
g = sin(x)**2 + cos(x)**2
print('g =',g)

simplify(g)
print('g =',g)

es = expand(sin(x+y), trig=True) # trig 指明是三角函数
print(es)
