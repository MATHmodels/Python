from scitools.StringFunction import StringFunction
import sys, math

def numerical_derivative(f, x, h=1E-5):
    return (f(x+h) - f(x-h))/(2*h)
    
f = StringFunction(sys.argv[1], independent_variable='x')
x = float(sys.argv[2])
print('数值微分:', numerical_derivative(f, x))
