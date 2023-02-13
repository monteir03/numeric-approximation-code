import math


lx=[math.pi/6.0,math.pi/4.0]
f=[0.57735,1.0]

x=math.pi/5

polinomio=0.0

for i in range(2):
    l=1.0
    for j in range(2):
        if i!=j:
            l = l*(x-lx[j])/(lx[i]-lx[j])
    polinomio+=f[i]*l

print(x)
print(round(polinomio,7
))
