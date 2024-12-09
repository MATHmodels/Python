a = [1, 2, 9, 5, 8, 9]
b = [3, 4, 6, 9, 9, 4]
c = a + b
print('列表 a 和 b 合并成一个列表 c =', c)
print('c 中 9 的个数为', c.count(9))
d = sorted(c)
print('d =', d)
k = d.index(c[3])
print('列表 c 中序号为 3 的元素在列表 d 中的位置 k =', k)
print('d 中序号为 k-1 的元素为', d[k-1])
print('列表 d 最后 5 个元素的和为', sum(d[-5:]))
