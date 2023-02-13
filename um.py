#rect


a=1
b=2
n=4
h=b-a/n
aprox=0
t=a

for i in range(n):
    aprox+=f(t)+h
    t+=h

erro= h/2*(b-a)*1derivmax
