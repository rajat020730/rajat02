
def Unique(list,n): 
    list2=[]
    for i in list: 
        if i not in list2: 
            list2.append(i) 
    return (list2)
list = [] 
n = int(input("Enter number of elements : "))
for i in range(0, n): 
    ele = int(input())
    list.append(ele) # adding the element 
print(Unique(list,n))