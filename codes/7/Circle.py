from math import pi

class Circle:
    def __init__(self, x0, y0, R):
        self.x0, self.y0, self.R = x0, y0, R
    def dump(self):
        print('Circle(x0=%g, y0=%g, R=%g)' % \
                     (self.x0, self.y0, self.R))
    def area(self):
        return pi*self.R**2
    def circumference(self):
        return 2*pi*self.R

def test_Circle():
    R = 2.5
    c = Circle(7.4, -8.1, R)
    expected_area = pi*R**2
    computed_area = c.area()
    diff = abs(expected_area - computed_area)
    tol = 1E-14
    assert diff < tol, 'bug in Circle.area, diff=%s' % diff
    expected_circumference = 2*pi*R
    computed_circumference = c.circumference()
    diff = abs(expected_circumference - computed_circumference)
    assert diff < tol, 'bug in Circle.circumference, diff=%s' % diff

test_Circle()

if __name__=='__main__':
    c = Circle(0, 0, 2)
    c.dump()
    print('area = %g' % c.area())
    print('circumference = %g' % c.circumference())
