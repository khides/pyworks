import sympy as sp

A=sp.Matrix([[1,1],
             [1,1],
             [2,1],
             [2,1],
             [3,1],
             [3,1],
             [4,1],
             [4,1]])

y=sp.Matrix([[0.8],
             [1],
             [2.2],
             [2],
             [3.2],
             [3],
             [3.8],
             [4]])

print(A.T.multiply(A).inv().multiply(A.T).multiply(y))