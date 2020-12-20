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

b=[a[0]]

for i in range(1,n):
    if i<0:
        b.append( b[i-1] * a[i])

    else:
        b.append(b[i-1]+(i*(math.fabs(a[i]))))

print(f"Масив Б={b}")


