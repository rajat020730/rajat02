def Check(a,b):
    if a%2==0 and b%2==0:
        return(a if a < b else b)
    elif a%2!=0 and b%2!=0:
        return(a if a>b else b)
a=int(input())
b=int(input())
print(Check(a,b))