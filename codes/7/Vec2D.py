class Vec2D:
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    def __ne__(self, other): return not self.__eq__(other)

if __name__=='__main__':
    u = Vec2D(0,1)
    v = Vec2D(1,0)
    a = u + v
    print(a)
    w = Vec2D(1,1)
    print(a == w)
    print(u - v)
    print(u*v)
    
    
    
