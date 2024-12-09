for i in range(1,101):
    # 需要跳过 7 的倍数、个位上是 7 的、以及十位上是 7 的数
    if i % 7 == 0 or i % 10 == 7 or int(i/10) % 10 == 7:
        print('%4s' %'', end='') # 跳过的数用空格占位
    else:
        print('%4d' % i, end='') 
    
    if i % 20 == 0: print()      # 每经过 20 个数换一行
