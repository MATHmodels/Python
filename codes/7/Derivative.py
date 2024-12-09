class Derivative:
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, float(h)
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

def test_Derivative():
    f = lambda x: a*x + b # 线性函数，和 h 无关
    a = 3.5; b = 8
    dfdx = Derivative(f, h=0.5)
    diff = abs(dfdx(4.5) - a)
    assert diff < 1E-14, \
           'bug in class Derivative, diff=%s' % diff

test_Derivative()

if __name__=='__main__':
    from math import sin, pi
    df = Derivative(sin)
    print("sin(pi)' = %g" % df(pi))

    def g(t):
        return t**3
    dg = Derivative(g)
    print("g(1)' = %g" % dg(1))
