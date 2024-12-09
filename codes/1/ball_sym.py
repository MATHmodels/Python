from sympy import *
t, v0, g, y = symbols('t v0 g y')
f = v0*t - Rational(1,2)*g*t**2

dydt = diff(f, t)
t1 = solve(dydt, t)[0]
print('小球到达最高点的时间为：%s\n' % t1)

t2 = solve(f-y,t)
print('小球到达某位置 y 的时间为：\n %40s 和 %s\n' % tuple(t2))

t3 = [ti.subs([(v0,5), (g,9.8), (y,1)]) for ti in t2]
print('v0 = 5 m/s, y = 1 m 相应的时间为：%.4f s 和 %.4f s' % tuple(t3))
