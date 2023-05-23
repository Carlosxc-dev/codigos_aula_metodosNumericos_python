def f(x):
    return x**3 - x**2 - x - 1

def isolamento(a, b, precisao):
  inter = []
  x = a
  while x <= b:
    if f(x) * f(x + precisao) < 0:
      inter.append((x, x + precisao))
    x += precisao
  for i in inter:
    print("\n intervalo: ", i)

def bisseccao(a, b, precisao):
  while abs(b - a) > precisao:
    x = (a+b) / 2
    if (f(a)*f(x)) > 0:
      a = x;
    else:
      b = x;
  print("Raíz: ", (a+b) / 2)
  print("\n\n")


a = -2
b = 2
precisao = 0.0005
isolamento(a, b, precisao)
bisseccao(a, b, precisao)