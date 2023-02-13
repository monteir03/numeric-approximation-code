#F (x ) = 0.123x − x = 0
#com erro absoluto ε = 5*10**−4
#usando bissecções sucessivas.

#math.e
#math.pi
#math.cos math.sen math.tan

#toooni


import math

def func(x):
    return 0.123*x-x

def findroot(f,a,b,eps):
    intervalo=b-a
    niter=0
    while(abs(intervalo)>abs(eps)):
        niter+=1
        m=(b+a)/2
        if(f(m)==0):
            intervalo=0
            m = (m//eps)*eps
            return m
        if(f(m)*f(a)<0):
            b=m
        elif(f(m)*f(b)<0):
            a=m
        intervalo=intervalo/2
    m = (m//eps)*eps

    return m

epsi=5*(10)**(-4)
a=0
b=1

print(findroot(func,a,b,epsi))
