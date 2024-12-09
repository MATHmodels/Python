Cdegrees = list(range(20, 45, 5))
Fdegrees = [9/5*C + 32 for C in Cdegrees]

# 按列嵌套，table1 中包含两列
table1 = [Cdegrees, Fdegrees]
print(table1)

# 按行嵌套，table2 中每一行为序偶对 [C, F]
table2 = [[C, F] for C, F in zip(Cdegrees, Fdegrees)]
print(table2)
