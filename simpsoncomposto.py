import math

a=1
b=2

h = (b-a)/n

l=f(a)+f(b)
t+=a+h

for i in range(1,n):
    if(i%2==0):
        l+=2*f(t)
    elif(i%2!=0):
        l+=4*(t)
    t+=h
l*=(h/3)


erro = -((h**(4))/180)*(b-a)*(maior 4 derivada)
