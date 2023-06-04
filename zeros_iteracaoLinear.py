import math

def f(x):
    return x**3 - 9*x +3

def g(x):
    return -3/(x**2 - 9)

def isolamento(a, b, prec):
  inter = []
  x = a
  while x <= b:
    if f(x) * f(x + prec) < 0:
      inter.append((x, x + prec))
    x += prec
  for i in inter:
    print("intervalo = ", i)

a = -10
b = 10
erro1 = 0.001
erro2 = erro1      
x0 = 0.32       #valor entre os intervalos obtido pelo isolamento



if math.fabs(f(x0)) < erro1:
    x = x0
  
def iteracao_linear(x0):
    k=1
    while True: 
        x1 = g(x0)
        if (math.fabs(f(x1)) < erro1) | (math.fabs(x1 - x0) < erro2):
            x = x1
            return print('convergiu para: {:.4f}'.format(x))
        x0 = x1
        k = k+1

print("\n")
isolamento(a, b, 0.05)
print("valor aleatorio escolhido entre o intervalo: ", x0)
iteracao_linear(x0)

print("\n")