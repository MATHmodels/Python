formula = input('请输入一个关于 x 的表达式: ')
exec("""
def f(x):
    return %s""" % formula)

while True:
    x = eval(input('请输入 x (退出请输入 None): '))
    if x is None: break
    print('f(%g) = %g' % (x, f(x)))
