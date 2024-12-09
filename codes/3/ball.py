def yfunc(t, v0):
    g = 9.81
    return v0*t - 0.5*g*t**2
    
y = yfunc(0.1, 6); print(y)

y = yfunc(0.1, v0=6); print(y)

y = yfunc(t=0.1, v0=6); print(y)

y = yfunc(v0=6, t=0.1); print(y)
