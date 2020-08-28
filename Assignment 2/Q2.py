def Check(x,a,b):
    if x in range(a,b+1):
        print("yes")
    else:
        print("no")
print("Enter the upper and lower range:")
a=int(input())
b=int(input())
print("Enter the number to be searched:")
x=int(input())
Check(x,a,b)