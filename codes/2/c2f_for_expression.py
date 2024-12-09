# somelist = [expression for element in otherlist]
n = 5
Cdegrees = [-5 + i*5 for i in range(n)]
Fdegrees = [9/5*C + 32 for C in Cdegrees]
print(Cdegrees, Fdegrees)
