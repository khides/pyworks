import sympy 

x=sympy.Symbol('x')
y=sympy.Symbol('y')
eq=x**3-x**2-3*x+3 + y
print(sympy.solve(eq,y))