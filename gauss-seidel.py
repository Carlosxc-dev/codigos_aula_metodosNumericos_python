import math

# faz a comparcao para achar se o valor e proximo da precisao
def comparar(x, y, precisao):
    soma = 0
    zip_object = zip(x, y)
    for list1_i, list2_i in zip_object:
        soma = soma + math.fabs(list1_i-list2_i)

    if (soma < precisao):
        return True
    else:
        return False

#funcao que resolve usando metodo de gauss-seidel
def gauss_seidel(A, b, max_iter, precisao):
    n = len(b)
    sol = True
    x = b.copy()
    for i in list(range(1, n+1, 1)):
        if (math.fabs(A[i-1][i-1]) > 0.0):
            x[i-1] = b[i-1]/A[i-1][i-1]
        else:
            sol = False
            break

    if (sol):
        print("Iteração 0")
        print("x = ", x)
        y = x.copy()
        iter = 0

        while (iter < max_iter):
            iter = iter + 1
            for i in list(range(1, n+1, 1)):
                s = 0
                for j in list(range(1, n+1, 1)):
                    if ((i-1) > (j-1)):
                        s = s + A[i-1][j-1]*y[j-1]
                    elif ((i-1) < (j-1)):
                        s = s + A[i-1][j-1]*x[j-1]

                y[i-1] = (1/A[i-1][i-1])*(b[i-1]-s)

            print("Iteração: ", iter)
            print("y = ", y)
            if comparar(x, y, precisao):
                x = y.copy()
                break
            x = y.copy()

    return x

#dados
A = [[10, 2,  1],
     [1, 5,  2],
     [2, 3, 10]]
b = [7, -8, 6]

#resolucao
print("x = ", gauss_seidel(A, b, 100, 0.000000001))
