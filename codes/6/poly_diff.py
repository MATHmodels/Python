def diff(p):
    dp = {}
    for index, coeff in p.items():
        if index != 0:
            dp[index - 1] = index*coeff
    return dp

p = {0: -3, 3: 2, 5: -1}
print(diff(p))
