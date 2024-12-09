def poly_list(poly, x):
    S = 0
    for power in range(len(poly)):
        S += poly[power]*x**power
    # S = sum(poly[i]*x**i for i in range(len(poly)))
    return S

p = [-1, 0, 1, 0, 0, 0, 0, 3]
x = 2
print('p(%g) = %g' % (x, poly_list(p,x)) )
