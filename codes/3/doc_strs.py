def C2F(C):
    """将摄氏度转化为华氏度"""
    return 9/5*C + 32

def line(x0, y0, x1, y1):
    """ 
    通过直线上的两点计算直线 y = a*x + b 的斜率和截距。
    x0, y0: 直线上的一个点 (floats)
    x1, y1: 直线上另一个点 (floats)
    返回: a, b (floats)
    """
    a = (y1 - y0)/(x1 - x0)
    b = y0 - a*x0
    return a, b
