combinations = [(black, green) for black in range(1, 7)
                               for green in range(1, 7)]
success = [black > green for black, green in combinations]
M = sum(success)
N = len(combinations)
print('概率: %.4f' % (M/N))
