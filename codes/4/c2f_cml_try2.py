import sys
try:                             
    C = float(sys.argv[1])      
except IndexError:    # 超出sys.argv索引 -> IndexError异常
    print('没有命令行参数C！'); sys.exit(1)
except ValueError:    # float转换失败 -> ValueError异常
    print('参数C必需是数字！'); sys.exit(1)
F = 9/5*C + 32
print('%gC = %.1fF' % (C, F))
