from math import log as ln

def present_amount(A0, p, n):
    return A0*(1 + p/(360.0*100))**n
    
def initial_amount(A, p, n):
    return A*(1 + p/(360.0*100))**(-n)
    
def days(A0, A, p):
    return ln(A/A0)/ln(1 + p/(360.0*100))
    
def annual_rate(A0, A, n):
    return 360*100*((A/A0)**(1.0/n) - 1)
    
def test_all_functions():
    A = 2.2133983053266699; A0 = 2.0; p = 5; n = 730
    A_cmpt = present_amount(A0, p, n)
    A0_cmpt = initial_amount(A, p, n)
    n_cmpt = days(A0, A, p)
    p_cmpt = annual_rate(A0, A, n)
    def feq(a, b, tolerance=1E-12):
        return abs(a - b) < tolerance
    success = feq(A_cmpt, A) and feq(A0_cmpt, A0) and \
              feq(p_cmpt, p) and feq( n_cmpt,  n)
    if success: print("测试通过！")
    assert success, "没试不通过！"

if __name__ == '__main__': # 当模块被直接运行时为真，否则为假
    test_all_functions()
