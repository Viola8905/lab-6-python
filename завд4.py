from math import fabs
n = int(input("Введіть кількість елементів масиву: "))

k= [float(input("{0}-ий елемент: ".format(i+1))) for i in range(n)]

a = int(input("Введіть а: "))
b = int(input("Введіть b: "))
f=[]
c=[]


c=[x*0  for  x  in  k  if fabs(x)>=a and fabs(x)<=b ]


for i in list(k):
     if fabs(i)>=a and fabs(i)<=b:
                             k.remove(i)

f=k+c
                             


print(f)




