import sys
a1 = eval(sys.argv[1])
d  = eval(sys.argv[2])
n  = eval(sys.argv[3])

Sn = n*a1 + n*(n-1)/2*d
print('首项为 %f，公差为 %f 等差数列的前 %d 项和为 %f' % (a1, d, n, Sn))
