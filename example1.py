n = int(input("enter no. of element"))
target = int(input("enter the target"))
print("enter elements")
a=[]

for i in range(n):
    num = int(input())
    a.append(num)
print(a)
for i in range(n):
    for j in range(n):
        if a[i]+a[j]==target:
            print(i,end=' ')
            print(j)
            break
