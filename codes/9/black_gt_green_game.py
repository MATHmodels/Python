import random
N = 10000
start_capital = 10
money = start_capital
for i in range(N):
    money -= 1      # 每局交 1 元
    black = random.randint(1, 6)
    green = random.randint(1, 6)
    if black > green:
        money += 2  # 黑>绿，赢 2 元
        
net_profit_total = money - start_capital
net_profit_per_game = net_profit_total/N
print('平均每局输赢数：%g元' % net_profit_per_game)
