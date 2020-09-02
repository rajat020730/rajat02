str1=""
str2=""
str3=""
str4=""
str5=""
str6=""
str7=""
str8=""
str9=""
def End_Check():
    if(str1!="" and str2!="" and str3!="" and str4!="" and str5!="" and str6!="" and str7!="" and str8!="" and str9!=""):
        print("IT IS A DRAW!!!")
        return 1
def show_Board():
    print("        ",str1,"|       ",str2,"|    ",str3)
    print("-------------------------------")
    print("        ",str4,"|       ",str5,"|    ",str6)
    print("-------------------------------")
    print("        ",str7,"|       ",str8,"|    ",str9)
show_Board()
def Check_win():
    win="VICTORY"
    lose="LOST"
    if ((str1==str2 and str2==str3 and len(str2)!=0) or (str1==str4 and str4==str7 and len(str4)!=0) or (str1==str5 and str5==str9 and len(str5)!=0) or (str2==str4 and str4==str8 and len(str2)!=0) or (str3==str6 and str6==str9 and len(str3)!=0) or (str7==str8 and str8==str9 and len(str8)!=0) or (str4==str5 and str5==str6 and len(str6)!=0) or (str3==str5 and str5==str7 and len(str7)!=0)):
        return (win)
    else:
        return(lose)
print("*********WELCOME PLAYERS!*********")
while(1):
    n=int(input("Player 1: Enter number"))
    if n==1:
        str1="X"
    elif n==2:
        str2="X"
    elif n==3:
        str3="X"
    elif n==4:
        str4="X"
    elif n==5:
        str5="X"
    elif n==6:
        str6="X"
    elif n==7:
        str7="X"
    elif n==8:
        str8="X"
    elif n==9:
        str9="X"
    else:
        print("Please enter only numbers between 1-9")
    show_Board()
    str=Check_win()
    if(str=="VICTORY"):
        print("PLAYER 1 WINS")
        break 
    if(End_Check()):
        break
    m=int(input("Player 2: Enter number"))
    if m==1:
        str1="O"
    elif m==2:
        str2="O"
    elif m==3:
        str3="O"
    elif m==4:
        str4="O"
    elif m==5:
        str5="O"
    elif m==6:
        str6="O"
    elif m==7:
        str7="O"
    elif m==8:
        str8="O"
    elif m==9:
        str9="O"
    else:
        print("Please enter only numbers between 1-9")
    show_Board()
    str=Check_win()
    if(str=="VICTORY"):
        print("PLAYER 2 WINS")
        break 
    if(End_Check()):
        break