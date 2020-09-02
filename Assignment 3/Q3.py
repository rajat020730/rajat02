def Rev(words):
    words.reverse()
   # return words

    
    
words=[]
n=int(input("Enter the number of words"))
for i in range(0,n):
    str=input()   
    words+=[str]
Rev(words)
str1 =' '
print(str1.join(words))
