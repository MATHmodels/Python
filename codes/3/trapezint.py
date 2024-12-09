from math import exp, pi, cos, sin, log

def trapezint(f, a, b, n):
    s = (f(a) + f(b)) / 2
    h = (b - a) / n
    for i in range(1, n):
        s += f(a + i * h)
    s *= h
    return s

# -----------------------------------------------------------------------------

print('trapezint( sin, 0, pi/2, 10) = %.8f' % trapezint(sin, 0, pi/2, 10))
print('trapezint(x**2, 0,    3,100) = %.8f' % trapezint(lambda x:x**2, 0, 3, 100))

# -----------------------------------------------------------------------------

def test_trapezint():
    tol = 1e-3
    funs = [(cos, 0, pi), (sin, 0, pi/2), (lambda x:x**2, 0, 3)]
    expected_values = [0, 1, 9]
    for f, expected in zip(funs, expected_values):
        computed = trapezint(f[0], f[1], f[2], 1000)
        msg = '%s: %s != %s' % (f[0].__name__, computed, expected)
        assert abs(expected - computed) < tol, msg
    print('通过测试！')

test_trapezint()
