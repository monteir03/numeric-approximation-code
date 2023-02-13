

#rectangulo composto

n=4
a=1
b=2

h=(b-a)/n
aprox=0
t=a
for i in range(n):
    aprox+=(h*f(t))
    t+=h

print(aprox)
maj = (h/2)*(b-a)*1derivadamaior
print(maj)
