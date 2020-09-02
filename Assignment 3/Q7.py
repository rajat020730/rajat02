def Check(list,n):
    sum = 0
    i=0
    while i<n:
        if list[i]==6:
            while(1):
                i=i+1
                if list[i]==9:
                    i=i+1
                    break
        else:
            sum+=list[i]
            i=i+1
    return sum

n=int(input("Enter the elements"))
list=[]
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(Check(list,n))