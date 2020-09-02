def Check(str):
    alp="abcdefghijklmnopqrstuvwxyz"
    for i in alp:
        if i not in str:
            print("Not anagram")
            return 0
    print("Anagram")
str=input()
Check(str)
