import math

def fx(x):
    return x**3 - 9*x + 3

def dfx(x):
    return 3*x**2 - 9

def isolamento(a, b, prec):
  inter = []
  x = a
  while x <= b:
    if fx(x) * fx(x + prec) < 0:
      inter.append((x, x + prec))
    x += prec
  for i in inter:
    print("intervalo = ", i)

a = -10
b = 10
erro1 = 0.0001
erro2 = erro1
x0 = -3.17     #valor entre os intervalos obtido pelo isolamento
y0 = 0.32
z0 = 2.81


if math.fabs(fx(x0)) < erro1:
    x = x0
  
def metodo_newton(x0):
    k=1
    while k < 20: 
        x1 = x0 - fx(x0) / dfx(x0)
        if (math.fabs(fx(x1)) < erro1) | (math.fabs(x1 - x0) < erro2):
            x = x1
            return print('convergiu para: {:.4f}'.format(x))
        x0 =x1
        k = k+1

print("\n")
isolamento(a, b, 0.05)
print("valor aleatorio escolhido entre o intervalo: ", x0)
metodo_newton(x0)
print("valor aleatorio escolhido entre o intervalo: ", y0)
metodo_newton(y0)
print("valor aleatorio escolhido entre o intervalo: ", z0)
metodo_newton(z0)
print("\n")