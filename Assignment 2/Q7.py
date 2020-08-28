def isevem(num):
    if num > 1:
        if num==2:
            return ("Prime")
        for i in range(2,num):
            if (num % i) == 0:
                 return ("Not Prime")
            else:
                print(num,"is a prime number")
                return ("Prime")
    else:
        return ("Not Prime")
n=int(input("Enter the limit:"))
tup=()
list=[]
for i in range(1,n+1):
    tup=(i,isevem(i))
    list.append(tup)
print(list)