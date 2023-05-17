A = [[3, 2, 4], [1, 1, 2], [4, 3, -2]]
B = [1, 2, 3]
sizeA = len(A)
result = []

def printMat():
    for i in range(sizeA): #linha
        print("[ ", end="" )
        for j in range(sizeA): #coluna
            print("{:5.2f} ".format(A[i][j]), end="")
        print("{:5.2f} ]".format(B[i]))
    print("\n")

#L2 = L2 – (a21/a11)*L1
#L3 = L3 - (a31/a11)*L1
def eliminacao():
    for k in range(sizeA):#linha
        if A[k][k] == 0:
            return None, "A diagonal principal não pode ter zeros"
        for i in range(k+1, sizeA):#coluna no intervalo de k
            mult = A[i][k] / A[k][k]
            for j in range(k+1, sizeA):
                A[i][j] = A[i][j] - mult * A[k][j]
            B[i] = B[i] - mult * B[k]
            A[i][k] = 0
    for k in range(sizeA-1, -1, -1):
        for i in range(k-1, -1, -1):
            mult = A[i][k] / A[k][k]
            for j in range(k-1, sizeA):
                A[i][j] = A[i][j] - mult * A[k][j]
            B[i] = B[i] - mult * B[k]
            A[i][k] = 0

def resolveSistema():
    x = [0]*sizeA
    for i in range(sizeA):
        x[i] = B[i] / A[i][i]
    return x


print("matriz original")
printMat()
eliminacao()
print("matriz com eliminacao ")
printMat()
x = resolveSistema()
print("Solucao: [ {:5.2f}, {:5.2f}, {:5.2f}]".format(x[0], x[1], x[2]))