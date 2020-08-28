def Mul(list,n):
    res=1
    for i in range(0,n):
        res=res*list[i]
    return res
list=[]
n=int(input("Enter the size of the list:"))
for i in range(0,n):
    a=int(input())
    list.append(a)
print(Mul(list,n))