import math
n=int(input("Введіть ціле значення n: "))
x=float(input("Введіть ціле значення x: "))
a=[]
b=[]
i=1
while i<=n:
    el=((i-1)**2)/((2*i**2)-1)+((math.factorial(i))*(math.sin(i*x)))
    a.append(el)
    i+=1

print("Масив A={0}".format(a))

for i in list(a):
    if i<0:
        el=math.factorial(i)
        b.append(el)
    else:
        el=(i)*(math.fabs(i))
        i+=1
        b.append(el)
        
print("Масив Б={0}".format(b))

