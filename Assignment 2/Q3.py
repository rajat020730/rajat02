def Count(str):
    up,low=0,0
    for i in range(0, len(str)):
        if (str[i].isupper()==1):
            up=up+1
        elif (str[i].islower()==1):
            low=low+1
    print("Upper case:",up,"Lower case:",low)
str=str(input())
Count(str)