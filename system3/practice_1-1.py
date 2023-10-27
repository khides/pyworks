import sympy
import numpy as np
from matplotlib import pyplot as plt

t = sympy.Symbol("t")
x = sympy.Function("x")
eq = sympy.Derivative(x(t), t, t) + 0.3*sympy.Derivative(x(t), t) + x(t) - sympy.sin(2*t)

ans = sympy.dsolve(eq, x(t), ics={x.subs(0):1, sympy.diff(x,t,1).subs(0):0}).rhs
print(ans)
ans.subs(0)




# timelst = np.arange(0, 100, 1)
# xlst = []
# for t in timelst:
#     xlst.append(ans.subs(t))

# ax, fig = plt.subplots()
# ax.plot(timelst, xlst)
# plt.show()