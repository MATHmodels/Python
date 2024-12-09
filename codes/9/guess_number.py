import random
number = random.randint(1, 100)
guess = eval(input('在 1-100 之间猜个数:'))
attempts = 1
while guess != number:
    if guess < number:
        print('低了!')
    else:
        print('高了!')
    guess = eval(input('重新猜:'))
    attempts += 1
print('猜对了，你猜了 %d 次' % attempts)
