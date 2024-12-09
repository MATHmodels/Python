v0, g, n = 5, 9.8, 101
t = [2*v0/g/(n-1)*i for i in range(n)]
y = [v0*x - 1/2*g*x**2 for x in t]

print('%6s %6s    ' % ('t', 'y') * 5)  # 打印表头
for i in range(n):
    print('%6.4f %6.4f'%(t[i], y[i]), end = '    ')
    if i % 5 == 0: print('')           # 每经 5 组数据换行（这里为方便排版）
    
# 按列嵌套，table1 中包含两列
table1 = [t, y]

# 按行嵌套，table2 中每一行为序偶对
table2 = [[ti, yi] for ti, yi in zip(t, y)]
