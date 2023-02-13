import math

def f(x):
    esta funçao  é a
    funçao de recorrecnia
    return f(x)

def aprox_X(f,x0,eps,nmax):
    x1=f(x0)
    erroiter=abs(x1-x0)
    while(erroiter>eps and i<=max):
        x0=x1
        x1=f(x0)
        errroiter=abs(x1)-abs(x0)
        i+=1
    return x1 #se for possivel
