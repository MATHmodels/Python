infile = open('data.txt', 'r')
mean, num = 0, 0
for line in infile:
    mean = mean + float(line)
    num = num + 1
infile.close()
mean = mean/num
print('均值为：%.2f' % mean)
