with open('pairs.dat', 'r') as infile:
    lines = infile.readlines()

pairs = [] 
for line in lines:
    words = line.split()
    for word in words:
        word = word[1:-1]  # 去掉括号
        n1, n2 = word.split(',')
        n1, n2 = float(n1), float(n2)
        pair = (n1, n2)
        pairs.append(pair)

import pprint
pprint.pprint(pairs)
