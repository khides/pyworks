import sympy as sp

a = sp.Symbol("a")
b = sp.Symbol("b")
c = sp.Symbol("c")
d = sp.Symbol("d")

eq1 = a - d + sp.Rational(1,2)
eq2 = b - a - sp.Rational(2,7)
eq3 = c - b - sp.Rational(2,7)
eq4 = a+b+c+d

print(sp.solve([eq1,eq2,eq3,eq4]))

x = sp.Rational(-3,14)
y = sp.Rational(-3,7)
a = sp.Rational(-19,56)
b = sp.Rational(-3,56)
c = sp.Rational(-13,56)
d = sp.Rational(9,56)

z = x*sp.Rational(6,5) +y*sp.Rational(1,2) + a*sp.Rational(1,2) + b*sp.Rational(4,5) + c*sp.Rational(1,2) + d*sp.Rational(1,5)

print(z)