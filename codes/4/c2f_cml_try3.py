import sys
def read_C():
    try: 
        C = float(sys.argv[1])
    except IndexError: 
        raise IndexError ('需要提供参数C')
    except ValueError:
        raise ValueError ('"%s"不是一个数字' % sys.argv[1])
    if C < -273.15:
        raise ValueError ('C = %g 不是一个合理的温度' % C)
    return C

try: 
    C = read_C()
except (IndexError, ValueError) as e:
    print(e); sys.exit(1)

F = 9.0*C/5 + 32
print('%gC = %.1fF' % (C, F))
