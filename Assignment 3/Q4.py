def Check(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10
n=int(input())
print(Check(n))
