def trapezoidal(f, a, x, n):
    h = (x-a)/n; I = (f(a)+f(x))/2
    for i in range(1, n):
        I += f(a + i*h)
    return I*h

class Integral:
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n = f, a, n
    def __call__(self, x):
        return trapezoidal(self.f, self.a, x, self.n)

def test_Integral():
    f = lambda x: 2*x + 5 # 线性函数积分，结果和 h 无关
    F = lambda x: x**2 + 5*x
    a, x = 2, 6
    I = Integral(f, a, n=4)
    diff = abs(I(x) - (F(x) - F(a)))
    assert diff < 1E-15, \
           'bug in class Integral, diff=%s' % diff

test_Integral()

if __name__=='__main__':
    from math import exp, sin
    def f(x):
        return exp(-x**2)*sin(10*x)
    a = 0; n = 200
    F = Integral(f, a, n)
    x = 1.2
    print(F(x))
