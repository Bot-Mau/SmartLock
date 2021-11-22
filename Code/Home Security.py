#Define the home member 
def member():
    print("Are you this home family member?")
    print("1. Yes")
    print("2. No")
    ch=int(input())
    if(ch==1):
        print("Choose one of the following member:")
        print("1. Chau")
        print("2. Suong")
        print("3. Triet")
        print("4. Nhat")
        print("5. None")
        ch=int(input())
        if (ch==1):
            print ("Welcome Home Chau.")
        elif (ch==2):
            print ("Welcome Home Suong")
        elif (ch==3):
            print ("Welcome Home Triet")
        else:
            print ("Welcome Home Nhat")
    else:
        print("You are an Outsider")
        Outsider()



#define An Guest
def Guest():
    print("Please input you name to clarify")
    ch=input()
    if(ch=="ngoc"):
        print("Welcome peNgoc")
    else:
        print("Not welcome here")





#Define the outsider
def Outsider():
    print("Are you invited by the home member ?")
    print("1. Yes")
    print("2. No")
    ch=int(input())
    if(ch==1):
       Guest()
    else :
        print("Your are not welcome here. GoodBye!!!")  


#define main
print ("welcome to my home")
print ("Please enter your name for permisson to enter the house")
member()
