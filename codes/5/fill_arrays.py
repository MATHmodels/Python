from numpy import sqrt, exp, pi, linspace, zeros

def h(x):
    return 1 / sqrt(2 * pi) * exp(-0.5 * x * x)
    
xmin, xmax, n = -4, 4, 11

# 使用循环
x, y = zeros(n), zeros(n)
for i in range(n):
    x[i] = xmin + (xmax-xmin)/(n-1)*i
    y[i] = h(x[i])
    
print('x =', x)
print('y =', y)

# 向量化
x = linspace(xmin, xmax, n)
y = h(x)
print('x =', x)
print('y =', y)

