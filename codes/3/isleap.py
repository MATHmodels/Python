def isleap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        return True
    else:
        return False

years = [1994, 1996, 2000, 2024]

for y in years:
    print('%d 年是润年'%y) if isleap(y) else print('%d 年不是润年'%y)
