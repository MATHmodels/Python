q = ('N', 'B', 'U', 315211, 818, 'Y', 'E', 'S')
q = list(q)                # 转为列表
q.remove('E')
q.insert(q.index('S'),'Y');  q.insert(q.index('S'),'D')
q = tuple(q); print(q)     # 转回元组并输出

p = ((q[0:3]), (q[3:5]), (q[5:])); print(p)
