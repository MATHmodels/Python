Cdegrees = [-20, -15, -10, -5,  0, 5]
index = 0

print('%5s %5s'%('C', 'F'))
while index < len(Cdegrees):
    C = Cdegrees[index]
    F = 9/5*C + 32
    print('%5d %5.1f' % (C, F))
    index += 1
