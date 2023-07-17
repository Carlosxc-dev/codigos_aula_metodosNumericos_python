def eliminacao(A, B):
    n = len(A)  
    for i in range(n-1):
        pivo = A[i][i]
        for j in range(i+1, n):
            aux = A[j][i] / pivo
            B[j] -= aux * B[i]
            for k in range(n):
                A[j][k] -= aux * A[i][k]

def substituição(A, B):
    n = len(A)  
    X = [0] * n
    for i in range(n-1, -1, -1):
        X[i] = B[i]
        for j in range(i+1, n):
            X[i] -= A[i][j] * X[j]
        X[i] /= A[i][i]

    return X

def gauss(A, B): 
    eliminacao(A, B)
    aux = substituição(A, B)
    return aux

def sistema():
    n = len(X)
    A = [[0] * (n+1) for _ in range(n)]
    for i in range(n):
        A[i][0] = 1
        for j in range(1, n):
            A[i][j] = X[i] ** j
        A[i][n] = F[i]
    coefic = gauss(A, F)
    return coefic

# entrada de dados
X = [0.9, 1, 1.3, 1.8, 2, 2.2]
F = [-0.105, 0, 0.262, 0.588, 0.693, 0.788]

# fazendo o sistema de equacoes 
n = len(X)
aux = sistema()
# Calcula f(1.4)
valor = 1.4
fx = sum(aux[i] * (valor ** i) for i in range(n))

print("resultado = {:.3f}".format(fx))
