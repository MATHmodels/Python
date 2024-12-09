from Line_Parabola import Line, Parabola

class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3
    def __call__(self, x):
        return Parabola.__call__(self, x) + self.c3*x**3

class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4
    def __call__(self, x):
        return Cubic.__call__(self, x) + self.c4*x**4

if __name__=='__main__':
    quartic = Poly4(1, 2, 3, 4, 5)
    print(quartic(10))
