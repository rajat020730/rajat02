n=int(input("Enter the number of rows :"))
for i in range(n):
    x=1
    for j in range(i):
        print(x,end=" ")
        x=x*(i-j)//(j+1)
    print("1")