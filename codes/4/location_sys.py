import sys
v0, t = float(sys.argv[1]), float(sys.argv[2])
y = v0*t + 1/2*9.8*t**2
print('v0 = %.2f m/s, t = %.2f s，y = %.2f m' % (v0, t, y))
