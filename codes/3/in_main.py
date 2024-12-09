from math import *            # 主程序语句

def f(x):                     # 主程序语句
    e = exp(-0.1*x)
    s = sin(6*pi*x)
    return e*s
    
x = 2                         # 主程序语句
y = f(x)                      # 主程序语句
print('f(%g)=%g' % (x, y))    # 主程序语句
