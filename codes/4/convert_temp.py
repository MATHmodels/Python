import sys

_usage = """
作为库载入其它程序的用法示例：
>>> from convert_temp import *
>>> C2F(21.3)
70.34

作为主程序在命令行调用的用法示例：
用法: python %s 21.3 C
输出：70.3 F 294.4 K
""" % sys.argv[0]

def C2F(C):
    F = 9/5 * C + 32
    return F

def F2C(F):
    C = 5/9 * (F - 32)
    return C

def C2K(C):
    K = C + 273.15
    return K

def K2C(K):
    C = K - 273.15
    return C

def F2K(F):
    K = F2C(F) + 273.15
    return K

def K2F(K):
    F = C2F(K - 273.15)
    return F

def test_conversion():
    eps = 1.0E-1
    success = abs(C2F(F2C(13))-13) < eps and abs(K2C(C2K(131))-131) < eps \
        and abs(K2F(F2K(143))-143) < eps
    msg = 'Conversion error!  Check functions.'
    assert success, msg

if sys.argv[1] == 'verify':
    test_conversion()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(_usage)
        raise IndexError('需要通过命令行输入温度值和相应温标')
    if sys.argv[2] == 'C':
        C = float(sys.argv[1])
        print('%g F %g K' % (C2F(C), C2K(C)))
    elif sys.argv[2] == 'F':
        F = float(sys.argv[1])
        print('%g C %g K' % (F2C(F), F2K(F)))
    elif sys.argv[2] == 'K':
        K = float(sys.argv[1])
        print('%g F %g C' % (K2F(K), K2C(K)))
