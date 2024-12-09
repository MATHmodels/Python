def N(x):
    if x < 0:
        return 0
    elif 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2 - x
    elif x >= 2:
        return 0
        
print('N(-0.2) =', N(-0.2))
print('N( 0.5) =', N( 0.5))
print('N( 1.2) =', N( 1.2))
print('N( 3.8) =', N( 3.8))

