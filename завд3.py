import math
n = int(input("Вкажіть вимір вектора: "))

x = [float(input("Задайте {0}-координату вектора: ".format(i+1))) for i in range(n)]

y = [float(input("Задайте {0}-координату вектора: ".format(i+1))) for i in range(n)]

d=0
c=0
f=0

for el in range (1):
    d=(x[0]*y[0])+(x[1]*y[1])+d

for el in range(n):
    c=(math.sqrt((x[0]**2)+(x[1]**2)))*(math.sqrt((y[0]**2)+(y[1]**2)))\
       
f=d/c

print(f)
