n=int(input("n="))
a=[int(input("a="))for i in range (n)]
b=[el for el in a if el<0 ]
print("найбільше від'ємне число =",max(b))
