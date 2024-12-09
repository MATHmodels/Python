from sympy import *
t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1,2)*g*t**2
dydt = diff(y, t)                      # 一阶导数               
print('dydt =', dydt)

print('acceleration:', diff(y, t, t))  # 二阶导数

y2 = integrate(dydt, t)                # 积分
print('y2 =', y2)

roots = solve(y, t)          # 求解 y = 0 时 t 的根
print('roots =', roots)

y.subs(t, roots[1])          # 代回验证
print('y =', y)
