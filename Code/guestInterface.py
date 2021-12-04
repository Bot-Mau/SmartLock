import main
import checker
import error
import gclass
import manageInterface

def editGuestCode():
    flag = True
    
    count = 2

    #print("Changing master passcode...\n")
    print ("Do you want to edit guestcode?")
    print("1. add guestcode")
    print("2. remove guestcode")
    print("3. no,just unlock")
    x=int(input())
    print("\n\n\n")
    if (x==1):
        while flag:

            enteredCode = input("Enter master passcode: ")
       
            if (checker.Checker(count,enteredCode) == 0):  # Use the checker class

            # Send newCode to OwnerClass to update master passCode
                gclass.add_guest()
                manageInterface.showMasterUI()  
        
                flag = False

            else:
                error.Error()  # Sending count number to the Error class to check for attempts
    elif(x==2):
        while flag:

            enteredCode = input("Enter master passcode: ")
       
            if (checker.Checker(count,enteredCode) == 0):  # Use the checker class

            # Send newCode to OwnerClass to update master passCode
                gclass.remove_guest()
                manageInterface.showMasterUI()  
        
                flag = False

            else:
                error.Error()
    else:
        main.Main(2)


