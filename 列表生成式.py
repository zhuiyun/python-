a=[i for i in range(1,18) if i%2==0]
print(a)
b=[i for i in range(3) for j in range(2)]
print(b)
c=[(i,j) for i in range(3) for j in range(2)]
print(c)

e=[1,2,3,4,4,5,6,1]
print(e)
d=set(e)
print(d)
e=list(d)
print(e)