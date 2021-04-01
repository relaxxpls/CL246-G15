import sympy as sp


x, y = sp.symbols('x y')

f = sp.Function('f')(x, y)

display(f.diff(x, y))

exp = x**2
exp


EQ1_1 = sp.Eq()

display(EQ1_1)
