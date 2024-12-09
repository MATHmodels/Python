import sys
if len(sys.argv) < 2:
    print('输入参数失败')
    sys.exit(1)  # 终止程序
C = float(sys.argv[1])
F = 9/5*C + 32
print('%gC = %.1fF' % (C, F))
