class IntervalMath:
    def __init__(self, lower, upper):
        self.lo, self.up = float(lower), float(upper)

    def __add__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a + c, b + d)

    def __sub__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a - d, b - c)

    def __mul__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(min(a*c, a*d, b*c, b*d),
                            max(a*c, a*d, b*c, b*d))

    def __truediv__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        if c*d <= 0: # [c,d] cannot contain zero:
            raise ValueError\
                  ('Interval %s cannot be denominator because '\
                   'it contains zero')
        return IntervalMath(min(a/c, a/d, b/c, b/d),
                            max(a/c, a/d, b/c, b/d))

    def __str__(self):
        return '[%g, %g]' % (self.lo, self.up)
    def __repr__(self):
        return 'IntervalMath(%g, %g)' % (self.lo, self.up)

if __name__ == '__main__':
    u = IntervalMath(-3,-2)
    v = IntervalMath(4,5)
    expr = ['u+v', 'u-v', 'u*v', 'u/v']
    for e in expr:
        print(e, '=', eval(e))
