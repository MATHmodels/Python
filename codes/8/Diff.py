class Diff:                # 基类
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h

class Forward1(Diff):      # 一阶前向差分的派生类
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h
    
class Backward1(Diff):     # 一阶后向差分的派生类
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Central4(Diff):      # 四阶中心差分的派生类
    def __call__(self, x):
        f, h = self.f, self.h
        return 4/3*(f(x+h)   - f(x-h))  /(2*h) - \
               1/3*(f(x+2*h) - f(x-2*h))/(4*h)

def _test_one_method(method):
    """Test method in string `method` on a linear function."""
    f = lambda x: a*x + b
    df_exact = lambda x: a
    a = 0.2; b = -4
    df = eval(method)(f, h=0.55)
    x = 6.2
    msg = 'method %s failed: df/dx=%g != %g' % \
          (method, df(x), df_exact(x))
    tol = 1E-14
    assert abs(df_exact(x) - df(x)) < tol

def test_all_methods():
    """Call _test_one_method for all subclasses of Diff."""
    # print(globals())
    names = list(globals().keys())  # all names in this module
    for name in names:
        if name[0].isupper():
            if issubclass(eval(name), Diff):
                if name != 'Diff':
                    _test_one_method(name)

test_all_methods()

if __name__ == '__main__':
    from math import * 
    dsin_forward1 = Forward1(sin)
    print(dsin_forward1(pi))

    dsin_central4 = Central4(sin)
    print(dsin_central4(pi))
