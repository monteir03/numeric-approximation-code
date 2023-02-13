import math

def ex12(erro):
    soma=0
    k=1
    termo=((-1)**k)*(k/((5**k)+10))
    while(abs(termo)>=erro):
        soma+=termo
        k+=1
        termo=((-1)**k)*(k/((5**k)+10))

    print(soma)

ex12(5*(10**(-4)))
