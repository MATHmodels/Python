import argparse
parser = argparse.ArgumentParser() # 创建参数解析器

# 定义命令行选项：参数选项、参数名、类型、默认值和帮助字符串
parser.add_argument('--v0', '--initial_velocity', 
        type=float, default=0.0, help='initial velocity')
parser.add_argument('--t',  '--time', 
        type=float, default=1.0, help='time')

# 读入命令行先项并进行解析
args = parser.parse_args()
v0, t= args.v0, args.t

y = v0*t + 1/2*9.8*t**2
print('v0 = %.2f m/s, t = %.2f s，y = %.2f m' % (v0, t, y))
