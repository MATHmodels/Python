n = 5
Cdegrees = []
Fdegrees = []
for i in range(n):
    Cdegrees.append(-20 + i*5)
    Fdegrees.append(9/5*Cdegrees[i] + 32)
print(Cdegrees, Fdegrees)
