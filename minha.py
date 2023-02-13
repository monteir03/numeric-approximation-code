import math


minha

def f(x):
    return 0.123**x-x

def minha(f,a,b,eps):
    m=a
    erroiter=abs(b-a)
    n=0
    while(abs(erroiter)>abs(eps)):
        m=(a+b)/2
        if(f(m)==0):
            return m
        if(f(a)*f(m)<0):
            b=m
        elif(f(b)*f(m)<0):
            a=m
        erroiter= erroiter/2.0

    return m
    #tendo em conta erro

ai=0.0
bi=1.0
epsi=5.0*(10**(-4))

print(minha(f,ai,bi,epsi))
