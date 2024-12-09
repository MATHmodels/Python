import numpy as np
def sic_bo(n=100000):
    big_wins = 0     # 押大获胜次数
    small_wins = 0   # 押小获胜次数
    casino_wins = 0  # 围骰次数（赌场获胜）

    for _ in range(trials):
        # 掷三个骰子
        dice = np.random.randint(1, 7, size=3)
        total = np.sum(dice)

        # 判断结果
        if dice[0] == dice[1] == dice[2]:  # 围骰
            casino_wins += 1
        elif total >= 11: # 押大
            big_wins += 1
        else:             # 押小
            small_wins += 1

    # 计算并返回胜率
    return big_wins/n, small_wins/n, casino_wins/n

trials = 100000
big_rate, small_rate, casino_rate = sic_bo(trials)

# 输出结果
print(f"在 {trials} 次游戏中：")
print(f"押大的胜率: {big_rate * 100:5.2f}%")
print(f"押小的胜率: {small_rate * 100:5.2f}%")
print(f"围骰的胜率: {casino_rate * 100:5.2f}%")

# -----------------------------------------------------------------------------

# 理论计算
combinations = [(i, j, k) for i in range(1, 7)
                          for j in range(1, 7)
                          for k in range(1, 7)]

big_wins = [(i+j+k>=11) for i, j, k in combinations if not (i==j==k)]
small_wins = [(i+j+k<=10) for i, j, k in combinations if not (i==j==k)]
casino_wins = [(i==j==k) for i, j, k in combinations]

n = len(combinations)
big_rate = np.sum(big_wins)/n
small_rate = np.sum(small_wins)/n
casino_rate = np.sum(casino_wins)/n

print("\n理论上：")
print(f"押大的胜率: {big_rate * 100:5.2f}%")
print(f"押小的胜率: {small_rate * 100:5.2f}%")
print(f"围骰的胜率: {casino_rate * 100:5.2f}%")
