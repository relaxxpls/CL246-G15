import sympy as sp


x, y = sp.symbols('x y')

f = sp.Function('f')(x, y)

display(f.diff(x, y))

exp = x**2
exp


t = sp.symbols('t')

T_R = sp.symbols('T_R')

Q_W = sp.Function('Q_W')(t)
# EQ1_1 = sp.Eq(M_R * T_R.diff(t), Q_W + Q_R + Q_D - Q_F - Q_iv)

display(T_R, Q_W)









