def double(x):     # 函数
    return 2*x
    
def test_double(): # 测试函数： 对 double(x) 函数进行测试
    tol = 1E-14 
    x_values = [3, 7, -2, 0, 4.5]
    expected_values = [6, 14, -4, 0, 9]
    for x, expected in zip(x_values, expected_values):
        computed = double(x)
        msg = '%s != %s' % (computed, expected)
        assert abs(expected - computed) < tol, msg

test_double() # 测试通过则什么也不输出！
