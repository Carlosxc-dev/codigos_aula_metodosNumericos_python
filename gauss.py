import numpy as np

#pivoteamento parcial
def pivoteamento(A, b):
    max = k
    for f in range(k+1, n):
        if abs(A[f][k]) > abs(A[max][k]):
            max = f
    #reposicionando
    A[k], A[max] = A[max], A[k]
    b[k], b[max] = b[max], b[k]

#eliminação de Gauss
def eliminacao(A, b):
    for i in range (k+1, n):            
        m = A[i][k] / A[k][k]
        A[i][k] = 0
        for j in range(k+1, n):
            A[i][j] -= m * A[k][j]
        b[i] -= m * b[k]

#retrosubstituição e resolução do sistema
def resolucao(A, b):
    x = [0, 0, 0]
    x[n-1] = b[n-1] / A[n-1][n-1]

    for k in range(n-1, -1, -1):
        s = 0
        for j in range(k, n):
            s += A[k][j] * x[j]
            x[k] = (b[k] - s) / A[k][k]
    print("esse e o reultado: ", x)

#dados de entrada
A = ([[3, 2, 4], [1, 1, 2], [4, 3, -2]]) 
b = ([1, 2, 3])
det = np.linalg.det(A)
n = len(A)

#determinante == 0 nao pode usar o metodo
if det == 0:   
  print("impossivel usar o método")
else:
    for k in range(0, n):
        if A[k][k] == 0:
            raise ZeroDivisionError("nao pode dividir por zero")
        else:
            pivoteamento(A, b)
            eliminacao(A, b)
    resolucao(A, b)
