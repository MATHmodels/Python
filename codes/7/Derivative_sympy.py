import sympy as sp
class Derivative_sympy:
    def __init__(self, f):
        self.x = sp.Symbol('x')
        self.sympy_dfdx = sp.diff(f(self.x), self.x)
    def __call__(self,n):
        func = sp.lambdify([self.x], self.sympy_dfdx)
        return func(n)

if __name__=='__main__':
    def g(t):
        return t**3
    def h(y):
        return sp.sin(y)
    dg = Derivative_sympy(g)
    dh = Derivative_sympy(h)
    print(dg(1)) #3*t**2 for t=1
    from math import pi
    print(dh(pi)) #cos(y) for y=pi
