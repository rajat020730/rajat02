def Check(list):
    i=0
    while i < len(list):
        if list[i]==0:
            j=i+1
          # print("@",j)
            while j < len(list):
                if list[j]==0:
                    k=j+1
                    #print("%",k)
                    while k <= len(list):
                        if list[k]==7:
                           # print("#",k)
                            return("True")
                        k=k+1
                j=j+1
        i=i+1
    return("False")
    
n=int(input("Enter the number of elemnts:"))
list=[]
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(Check(list))