from datetime import datetime
def read_file(filename):
    infile = open(filename, 'r')
    infile.readline() # 跳过第一行
    dates = []; prices = []
    for line in infile:
        words = line.split(',')
        dates.append(words[0])
        prices.append(float(words[-1]))
    infile.close()
    dates.reverse(); prices.reverse()
    dates = [datetime.strptime(_date, '%Y-%m-%d').date()
             for _date in dates]
    prices = np.array(prices)
    return dates, prices

# 读入股价数据并绘制数据
import glob, numpy as np, matplotlib.pyplot as plt
dates = {};  prices = {}
filenames = glob.glob('stockprices_*.csv')
for filename in filenames:
    company = filename[12:-4]
    dates[company], prices[company] = read_file(filename)

for company in prices:
    x = dates[company]
    y = np.log(prices[company])
    plt.plot(x, y, label=company)

plt.xlabel('year')
plt.ylabel('ln(prices)')
plt.legend(); plt.show()


#plt.savefig('stockprices.pdf')

