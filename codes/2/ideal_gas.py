n = 40     # [mol] 物质的量
T = 250    # [K] 温度
R = 8.3145 # [J/(K mol)] 理想气体常数
m = 51

p = [100000 + 100000/(m-1)*i for i in range(m)]
V = [n*R*T/pi for pi in p]

print('%7s %7s  ' % ('p (kPa)', 'V (m^3)') * 5)  # 打印表头
for i in range(m):
    print('%7.2f %7.4f'%(p[i]/1000, V[i]), end = '  ')
    if i % 5 == 0: print('')           # 每经 5 组数据换行（这里为方便排版）
