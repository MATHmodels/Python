a1 = eval(input('请输入首项：a1 = '))
d  = eval(input('请输入公差： d = '))
n  = eval(input('请输入项数： n = '))

Sn = n*a1 + n*(n-1)/2*d
print('首项为 %f，公差为 %f 等差数列的前 %d 项和为 %f' % (a1, d, n, Sn))
