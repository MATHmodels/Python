Cs = list(range(20, 45, 5))
Fs = [9/5*C + 32 for C in Cs]
table = [[C, F] for C, F in zip(Cs, Fs)]

for C, F in table:      # 遍历全部
    print('%5.0f %5.1f' % (C, F))

print('\n--------------\n')

for C, F in table[1:3]: # 遍历部分
    print('%5.0f %5.1f' % (C, F))
