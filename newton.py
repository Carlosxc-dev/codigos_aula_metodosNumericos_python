import numpy as np
from numpy import linalg as lin


#dados
x0 = [-1, -2]
max_iter = 30 
iter = 0 
precisao = 0.001 
div = 10**20

def F(x) :
    n = len(x)
    b = [0]*n
    b[0] = 4*x[0] - x[0]**3 + x[1]
    b[1] = -(x[0]**2)/9 + (4*x[1] - x[1]**2)/4 + 1
    return b

def J(x):
    A = [[0,0], [0,0]]
    A[0][0] = 4 - 3*x[0]**2
    A[0][1] = 1
    A[1][0] = (-2*x[0])/9
    A[1][1] = 1 - x[1]/2
    
    return A

while(iter < max_iter):
    A = np.array(J(x0))
    b = np.array(F(x0))
    s = lin.solve(A, -b)
    x1 = np.array(x0) + s
    print("Repeticao", iter, ": ", x0)
    
    if(lin.norm(s, np.inf) < precisao) | (lin.norm(b, np.inf) < precisao):
        print("funcao convergiu")
        print("Precisao total: ", lin.norm(s, np.inf))
        break
    if(lin.norm(b, np.inf) > div):
        print("funcao divergiu")
        break
    
    x0 = x1
    iter += 1
