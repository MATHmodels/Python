class Line:
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1
    def __call__(self, x):
        return self.c0 + self.c1*x
    def table(self, L, R, n): # 返回 L，R 之间 n 个点的表格
        s = '%4s %4s\n' % ('x', 'y')
        import numpy as np
        for x in np.linspace(L, R, n):
            s += '%4g %4g\n' % (x, self(x))
        return s

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2
    def __call__(self, x):
        return Line.__call__(self, x) + self.c2*x**2

if __name__=='__main__':
    p = Parabola(1, -2, 2)
    print('y(2) =', p(2))
    print(p.table(0, 1, 3))

