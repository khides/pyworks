import sympy 
sympy.init_printing()###sqrtを表示する
rows=[[0,1,0,0],
      [0,0,1,0],
      [0,0,0,1],
      [-4,0,5,0]]
mat=sympy.Matrix(rows)
print(mat)

print(mat.T)
print(mat)
mat2=mat.T
print(mat2)
rows=[[1],
      [2],
      [3]]
vec=sympy.Matrix(rows)
rows=[[2],
      [3],
      [4]]
vec2=sympy.Matrix(rows)
print(vec)
print(vec2)
print('\n')

#行列式を求める
print('行列式')
print(mat.det())
print('\n')

#逆行列を求める
print('逆行列')
print(mat**(-1))
print(mat.inv()) 
print(mat*mat.inv())
print('\n')

#階段行列に変形
print('階段行列')
rows=[[1,-1,sympy.Rational(1,2),11],
      [1,sympy.Rational(1,3),-1,4],
      [1,-3,-1,14],]
mat3=sympy.Matrix(rows)
print(mat3.rref())
print('\n')

#固有値
print('固有値')
print(mat.eigenvals())
print('\n')

#固有ベクトルを求める
print('固有ベクトル')
print(mat.eigenvects())
print(type(mat.eigenvects()))
print('\n')

#対角化
print('対角化')
P,D=mat.diagonalize()
print('正則行列')
print(P)
print('対角行列')
print(D)
print('確認')
print(P*D*(P**-1))
print('\n')



print('matrix2numpy')
X=sympy.matrix2numpy(mat)
print(X)
print(type(X))
print('')


print('参照')
X=mat[1,2]
print(X)
print(type(X))
print('')

print('余因子行列')
X=mat.adjugate()
print(X)
print(type(X))
print('')


print('簡略化')
X=sympy.simplify(mat)
print(X)
print(type(X))
print('')

print('随伴行列')
X=mat.adjoint()
print(X)
print(type(X))
print('')


print('shape')
X=mat.shape
print(X)
print(type(X))
print('')

print('copy')
X=mat.copy()
print(X)
print(type(X))
print('')

print('reshape')
X=mat.reshape(2,8)
print(X)
print(type(X))
print('')

print('tolist')
X=mat.tolist()
print(X)
print(type(X))
print('')

print('行列積')
X=mat.multiply(mat2)
print(X)
X=mat*mat2
print(X)
print(type(X))
print('')

print('アダマール積')
X=sympy.matrix_multiply_elementwise(mat,mat2)
print(X)
print(type(X))
print('')

print('ones')
X=sympy.ones(4,4)
print(X)
print(type(X))
print('')

print('zeros')
X=sympy.zeros(4,4)
print(X)
print(type(X))
print('')

print('eye')
X=sympy.eye(4)
print(X)
print(type(X))
print('')

print('外積')
X=vec.cross(vec2)
print(X)
print(type(X))
print('')

print('norm')
X=mat.norm()
print(X)
print(type(X))
print('')

print('疑似逆行列')
X=mat.pinv()
print(X)
print(type(X))
print('')

print('QR分解')
X=mat.QRdecomposition()
print(X)
print(type(X))
print('')

print('var')
X=sympy.var('a,b')
print(X)
print(type(X))
print('')



#方程式に代入
print('因数分解')
x=sympy.Symbol('x')
y=sympy.Symbol('y')
eq=x**3-x**2-3*x+3
print(type(eq))
print(eq.subs(x,1))
print(type(eq.subs(x,1)))

#方程式を因数分解
print('因数分解')
fac=sympy.factor(eq)
print(fac)

#方程式を展開
print('展開')
ex=sympy.expand(fac)
print(ex)

#方程式を解く
print('方程式を解く')
print(sympy.solve(eq))

#連立方程式を解く
print('連立方程式を解く')
eq1=3*x+5*y-29
eq2=x+y-7
print(sympy.solve([eq1,eq2]))

#微分
print('微分')
print(sympy.diff(eq))

#偏微分
print('偏微分')
eq3=x**3+y**2-y
print(sympy.diff(eq3,x))
print(sympy.diff(eq3,y))

#積分
print('積分')
print(sympy.integrate(eq))

#線形微分方程式を解く
print('線形微分方程式を解く')
sympy.init_printing(False)
f=sympy.Function('f')
eq4=sympy.Derivative(f(x),x,x)+9*f(x)
print(sympy.dsolve(eq4,f(x)))

#非線形微分方程式を解く
print('非線形微分方程式を解く')
eq5=sympy.sin(x)*sympy.cos(f(x))+sympy.cos(x)*sympy.sin(f(x))*f(x).diff(x)
print(sympy.dsolve(eq5,f(x)))


#連立微分方程式を解く
print('連立微分方程式を解く')
from sympy.solvers.ode.systems import dsolve_system
g=sympy.Function('g')
eqs=[f(x).diff(x)-g(x),g(x).diff(x)-f(x)]
print(dsolve_system(eqs))