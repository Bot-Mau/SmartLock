import time

def Register():
    print("enter master code")
    mastercode = int(input())
    return(mastercode)


def Interface():
    print("enter passcode below: ")
    password = int(input())
    return(password)


def Checker(password, mastercode, guestcode):
    if(password == mastercode): 
        Unlock()
        return(0)
    else: 
        for code in guestcode:
            if (password == code):
                Unlock()
                return(1)
    return(2)


def Unlock():
    print("the door unlock")


def Owner(mastercode):
    print("Do you want to manage?")
    print("1. mastercode")
    print("2. guestcode")
    print("3. see guest checklog")
    print("4. No!!! Just unlock the door")
    x = int(input())
    if (x == 1):
        a = ManageOwner()
        mastercode = a
        Main(2, mastercode, gc)
    elif (x == 2):
        ManageGuest()
    elif (x == 3):
        Checklog()
    else:
        return (mastercode)


def ManageOwner():
    print("1. change master code")
    print("2. go back!")
    x = int(input())
    if (x == 1):
        print("enter new master code")
        newcode = int(input())
        print("new master code is: ", newcode)
        return(newcode)
    else:
        Owner(mastercode)
        return(mastercode)


def ManageGuest():
    print("1. add guest code")
    print("2. change guest code")
    print("3. delete guest code")
    print("4. go back!")
    x = int(input())
    if (x == 1):
        n=0
        while(guestcode[n] != 0):
            n += 1
        print("enter new guest code")
        guestcode[n] = int(input())
        Owner()
    elif (x == 2):
        print("list of guest code")
        n = 0
        while(n < 10):
            print(n, ". ", guestcode[n])
            n += 1
        print("choose code you want to change")
        a = int(input())
        print("new guest code ", a ," is: ")
        guestcode[a]=int(input())
        Owner()
    elif (x == 3):
        print("list of guest code")
        n = 0
        while(n < 10):
            print(n, ". ", guestcode[n])
            n += 1
        print("choose code you want to delete")
        a = int(input())
        print("guest code you want to delete is: ", guestcode[a])
        del guestcode[a]
        Owner()
    elif (x == 4):
        Owner()


def Checklog():
    return()

def Error():
    print("You have input the wrong passcode")  


def Alert(count):
    print(" You have ", count ,"attempt(s) left")

def Attempts(count):
    if (count > 0):
        count -= 1
        return (count)
    else:
        Lockdown()
        return (0)

def Lockdown():
    print("the door lock, plase enter right passcode after 5s")
    time.sleep(5)

def Main(count, mastercode, guestcode):
    password = Interface()
    check = Checker(password, mastercode, guestcode)
    if (check == 0):
        Owner(mastercode)
        Main(2, mastercode, guestcode)
    elif (check == 1):
        Main(2, mastercode, guestcode)
    else:
        Error()
        Alert(count)
        count = Attempts(count)
        Main (count, mastercode, guestcode)


count = 2
guestcode = [0] * 10
mastercode = Register()
Main (count, mastercode, guestcode)