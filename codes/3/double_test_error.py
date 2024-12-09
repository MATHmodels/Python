def double(x): return x**2  # 应为 2*x，假装写错了
    
def test_double(): # 测试函数： 对 double(x) 函数进行测试
    x = 4; computed = double(x); expected = 8
    msg = '测试输出 %s, 期望输出 %s' % (computed, expected)
    assert computed == expected, msg
    
test_double()
