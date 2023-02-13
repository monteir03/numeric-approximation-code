import math


def ex12(erro):
    n=1
    termo=1/2 #n=1
    soma=termo
    termo_seg= termo*(1/(2*(2*n+1)))
    n=2
    while(termo_seg>=erro):
        soma+=termo_seg
        n+=1
        termo_seg=sg*(1/(2*(2*n+1)))
    print(soma)



ex12(5*(10**(-4)))
