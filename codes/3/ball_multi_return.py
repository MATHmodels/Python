def yfunc(t, v0):
    g = 9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t # 计算 y 对 t 的导数
    return y, dydt  # 实际上，返回多个值时返回的一个元组

print(yfunc(0.6, 3))

position, velocity = yfunc(0.6, 3)
print(position, velocity)
