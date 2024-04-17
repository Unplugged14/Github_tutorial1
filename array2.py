a=[1,2,3]
b=[4,5,6]

for i in range(len(a)):
    a[i]=b[i]+a[i]

print(a)