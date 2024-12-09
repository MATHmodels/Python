import sympy as sym; from diff import * # 载入 diff.py 
x_value = x         # 存一下 x 的值，x 将被用作符号变量
x = sym.symbols('x') 
formula = sym.sympify(str(f))           # 将 f 转换为 表达式
dfdx = sym.diff(formula, x)             # 符号微分
dfdx_value = dfdx.subs(x, x_value)      # 用 x_value 替换 x
print('精确微分:', dfdx_value)
print('微分表达式:', dfdx)
