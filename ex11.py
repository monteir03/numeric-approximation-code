import math

def ex11(erro):
    n=0
    termo=(((-1)**n)*(0.5**(2*n)))/math.factorial(n)
    soma=0
    while(abs(termo)>=erro):
        soma+=termo
        n+=1
        termo=(((-1)**n)*(0.5**(2.0*n)))/(math.factorial(n))
    print(soma)

ex11(10**(-9))
