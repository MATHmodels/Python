def grade(score):
    if 90<=score<=100:
        return 'A'
    elif 80<=score<90:
        return 'B'
    elif 70<=score<80:
        return 'C'
    elif 60<=score<70:
        return 'D'
    else:
        return 'E'

# ----------------------------------------------------------------------------

from random import randint

scores = [randint(0,100) for i in range(20)]   # 随机生成 20 个 0-100 的分数
grades = [grade(score) for score in scores]    # 计算相应的等级

for s in scores: print('%4d' % s, end='')
print('')
for g in grades: print('%4s' % g, end='')
