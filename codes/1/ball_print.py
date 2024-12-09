v0 = 5
g = 9.8
t = 0.6 
y = v0*t - 1/2 * g*t**2
print("""At t = %f s, a ball with
initial velocity v0 = %.3E m/s
is located at the height %.2f m.""" % (t, v0, y))
