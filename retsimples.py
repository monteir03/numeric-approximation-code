import math

a=1
b=2

def f(x):
    return math.e**(x);

# retangulo simples

aprox = (b-a)*f(a)
print(aprox)
erro = ((b-a)**2)/2

if f(a)>f(b):
    maxderivada = f(a)
else
    maxderivada = f(b)

erro*=maxderivada
print(erro)
