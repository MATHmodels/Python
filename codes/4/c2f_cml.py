import sys
# 命令行参数存放在 sys.argv 列表中，sys.argv[0] = 'c2f_cml.py'
C = float(sys.argv[1])
F = 9/5*C + 32
print(F)
