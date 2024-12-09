import sys
try:                             # 如果 try 块中出现错误，程
    C = float(sys.argv[1])       # 序会抛出一个异常，并马上
except:                          # 转入到 except 块中执行
    print('输入参数失败')              
    sys.exit(1)  # 终止程序
F = 9/5*C + 32
print('%gC = %.1fF' % (C, F))
