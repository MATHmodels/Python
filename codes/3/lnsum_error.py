def L(x, n):
    s = 0
    for i in range(1, n+1):
        s += 1/i * (x/(1+x))**i
    return s
    
def L2(x, n):
    s = L(x, n)  # 调用之前定义的 L(x, n) 函数
    first_neglected_term = (1/(n+1))*(x/(1+x))**(n+1)
    from math import log
    exact_error = log(1+x) - s
    return s, first_neglected_term, exact_error
    
x = 1.2; n = 100
value, approx_error, exact_error = L2(x, n)
print('%.4f %.2e %.2e'%(value, approx_error, exact_error))
