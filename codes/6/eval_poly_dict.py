def poly_dict(poly, x):
    S = 0
    for power in poly: 
        S += poly[power]*x**power
    # S = sum(poly[power]*x**power for power in poly)
    return S 

p = {0: -1, 2: 1, 7: 3}
x = 2
print('p(%g) = %g' % (x, poly_dict(p,x)) )

