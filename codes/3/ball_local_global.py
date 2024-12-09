def yfunc(t):
    print('1. 局部变量 t:', t)
    g = 9.81
    t = 0.1
    print('2. 局部变量 t:', t)
    return v0*t - 0.5*g*t**2

t = 0.6
v0 = 2
print(yfunc(t))
print('1. 全局变量 t: %.1f\n' % t)

print(yfunc(0.3))
print('2. 全局变量 t: %.1f\n' % t)
