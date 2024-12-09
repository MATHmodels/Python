from Diff import Diff

class Central2(Diff):      # 二阶中心差分的派生类
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)

class Central6(Diff):      # 六阶中心差分的派生类
    def __call__(self, x):
        f, h = self.f, self.h
        return 3/2 *(f(x+h)   - f(x-h))  /(2*h) - \
               3/5 *(f(x+2*h) - f(x-2*h))/(4*h) + \
               1/10*(f(x+3*h) - f(x-3*h))/(6*h)

class Forward3(Diff):      # 三阶前向差分的派生类
    def __call__(self, x):
        f, h = self.f, self.h
        return (-1/6*f(x+2*h) + f(x+h) - 0.5*f(x) - \
                 1/3*f(x-h))/h

if __name__ == '__main__':
    from math import * 
    dsin_central2 = Central2(sin)
    print(dsin_central2(pi))

    dsin_central6 = Central6(sin)
    print(dsin_central6(pi))
