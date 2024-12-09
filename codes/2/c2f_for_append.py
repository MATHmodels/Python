Cdegrees = [-20, -15, -10, -5,  0, 5]
Fdegrees = [] # 初始化为空列表

for C in Cdegrees:
    F = 9/5*C + 32
    Fdegrees.append(F)
    
print(Fdegrees)
