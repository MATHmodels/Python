def yfunc(t, v0):
    g = 9.81
    return v0*t - 0.5*g*t**2

g, v0, t = 10, 5, 0.6
y = yfunc(t, 3)
print('y = %.1f' % y)
print('g = %.1f' % g)
