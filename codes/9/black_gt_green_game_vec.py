import numpy as np
N = 10000
r = np.random.randint(1, 7, size=(2,N))
start_capital = 10
money = start_capital - N
black, green = r[0,:], r[1,:]
M = np.sum(black > green)
money += 2*M
net_profit_total = money - start_capital
net_profit_per_game = net_profit_total/N
print('平均每局输赢数：%g元' % net_profit_per_game)

