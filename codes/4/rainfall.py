infile = open('rainfall.txt', 'r')
months, values = [], []
for line in infile:
    words = line.split()  # 将分字符串切分成词
    if words[0] != 'Year':
        months.append(words[0])
        values.append(float(words[1]))
    else:
        avg = float(words[1])
print('每月平均降雨量如下（mm）：')
for month, value in zip(months, values):
    print('%4s %5.1f' % (month, value))
print('每年平均降雨为（mm）：', avg)
