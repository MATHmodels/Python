def L(x, n):
    s = 0
    for i in range(1, n+1):
        s += 1/i * (x/(1+x))**i
    return s

def table(x):
    print('%4s  L(n,%g)' % ('n', x))
    for n in [1, 10, 100]:
        v = L(x, n)
        print('%4d %7.4f' % (n, v))
        
table(10)
