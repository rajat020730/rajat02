def Palin(str):
    str2= str[::-1]
    if str==str2:
        print("Palindrome")
    else:
        print("NOT Palindrome")

str=str(input("Enter the string:"))
Palin(str)