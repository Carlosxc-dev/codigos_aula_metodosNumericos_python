import numpy as np
import matplotlib.pyplot as plt

# Definindo a entrada u(t)
def u(t):
    return np.piecewise(t, [t<0, t>=0], [0, 1])

# Definindo a resposta natural do sistema
def yh(t, a, b):
    c1 = (5*a - b)/4
    c2 = (3*b - 5*a)/4
    return c1*np.exp(-t) + c2*np.exp(-2*t)

# Definindo a resposta forçada do sistema
def yp(t):
    return 1/5 - 1/5*np.exp(-5*t)

# Definindo a resposta completa do sistema
def y(t, a, b):
    return yh(t, a, b) + yp(t)

# Gerando o gráfico da resposta do sistema
t = np.linspace(0, 10, 1000)
y1 = y(t, 0, 1)
plt.plot(t, y1, label='a=0, b=1')
plt.xlabel('Tempo')
plt.ylabel('Resposta')
plt.title('Resposta do sistema')
plt.legend()
plt.show()
