def sumCheck(sum,a,b,c):
    if sum < 21:
        return sum
    elif sum > 21 and (a==11 or b==11 or c==11):
        sum-=10
        return sum
    else:
        return "BUST"
a,b,c=[int(x) for x in input().split()] 
sum=int(a+b+c)
print(sumCheck(sum,a,b,c))
