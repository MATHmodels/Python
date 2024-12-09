import sys; import sympy as sym
from scitools.StringFunction import StringFunction

def numerical_integrate(f, a, b, n=100):
    h = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a+i*h+h/2)
    return h*s
    
f = StringFunction(sys.argv[1], independent_variable='x') # 仅此行有差别
a = float(sys.argv[2])
b = float(sys.argv[3])
n = int(sys.argv[4])
print('数值积分:', numerical_integrate(f, a, b, n))

x = sym.symbols('x') 
formula = sym.sympify(sys.argv[1])
intf = sym.integrate(formula, x)
intf_value = intf.subs(x, b) - intf.subs(x, a)
print('精确积分:', intf_value)
print('积分表达式:', intf)
