def f(x):
    return x**3 - x**2 - x - 1

def posInt(a, b, prec):
  inter = []
  x = a
  while x <= b:
    if f(x) * f(x + prec) < 0:
      inter.append((x, x + prec))
    x += prec
  for i in inter:
    print("Possível intervalo:")
    print(i)

def bisseccao(a, b, prec):
  while abs(b - a) > prec:
    x = (a+b) / 2
    if (f(a)*f(x)) > 0:
      a = x;
    else:
      b = x;
  print("A raíz é:")
  print((a+b) / 2)


a = -2
b = 2
prec = 0.00005
posInt(a, b, prec)
bisseccao(a, b, prec)