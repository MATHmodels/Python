def yfunc(t):
    g = 9.81
    global v0       # 若注释掉这一行，输出结果会变成什么？
    v0 = 9
    return v0*t - 0.5*g*t**2
   
v0 = 2
print('1. v0:', v0)

yfunc(0.8)
print('2. v0:', v0)
