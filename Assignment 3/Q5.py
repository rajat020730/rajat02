def Check(list):
    for i in range(0,len(list)):
        if list[i]==3 and list[i+1]==3:
            return "true"
    return "false"
n=int(input("Enter the number of elemens"))
list=[]
for i in range(0,n):
    element=int(input())
    list.append(element)
print(Check(list))