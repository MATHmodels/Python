import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--a1', '--initial term',
       type=float, default=2, help='首项')
       
parser.add_argument('--d', '--common difference',
       type=float, default=3, help='公差')
       
parser.add_argument('--n', '--number of terms',
       type=int, default=10, help='项数')

args = parser.parse_args()
a1, d, n = args.a1, args.d, args.n

Sn = n*a1 + n*(n-1)/2*d
print('首项为 %f，公差为 %f 等差数列的前 %d 项和为 %f' % (a1, d, n, Sn))
