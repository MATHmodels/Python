def diff2(f, x, h=1E-6): # 参数 f 为函数
    r = (f(x-h) - 2*f(x) + f(x+h))/h**2
    return r
    
def g(t): return t**(-6)
    
for k in range(1,11):
    h = 10**(-k)
    g2 = diff2(g, 1, h)
    print('h=%.0e: %.2f' % (h, g2))
