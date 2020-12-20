import math

n = int(input("Вкажіть вимір вектора: "))

x = [float(input("Задайте {0}-координату вектора: ".format(i + 1))) for i in range(n)]

y = [float(input("Задайте {0}-координату вектора: ".format(i + 1))) for i in range(n)]

d = 0
c = 0
f = 0
z=[]
g=[a*a for a in x]
z=[a*a for a in y]


for i in range(n):
    d = (x[i] * y[i]) + d


f = d / (math.sqrt(sum(g))*(math.sqrt(sum(z))))
print(f)
