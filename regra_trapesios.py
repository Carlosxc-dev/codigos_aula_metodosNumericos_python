def f(x):
    return -x**2 + 3 * x**3 - 7 * x

def trapezio(a, b, n):
    h = (b - a) / n
    x = a
    int = (f(a) + f(b)) / 2
    for _ in range(1, n):
        x += h
        int += f(x)
    
    return int*h

resp = trapezio(1, 7, 1000)
print(resp, 3)