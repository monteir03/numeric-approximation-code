import math

def ex13(erro):
    n=1
    x=1.1
    termo=(-1)**(n+1)*x**(2*n-1)/math.factorial(2*n-1)
    seno=0
    while(abs(termo)>=erro):
        seno+=termo
        n+=1
        termo=(-1)**(n+1)*x**(2*n-1)/math.factorial(2*n-1)

    return seno

def coss(erro):
    er=erro
    seni=ex13(er)
    cos=(1-seni**2)**(1/2)
    print(cos)

coss(10**(-4))
