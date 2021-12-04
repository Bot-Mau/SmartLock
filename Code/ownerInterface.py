import main
import checker
import error
import master_class
import manageInterface

def changeMasterCode():
    flag = True
    
    count = 2

    #print("Changing master passcode...\n")
    print ("Do you want to change your mastercode?")
    print("1. yes")
    print("2. no, just unlock")
    x=int(input())
    print("\n\n\n")
    if (x==1):
        while flag:

            enteredCode = input("Enter master passcode: ")
       
            if (checker.Checker(count,enteredCode) == 0):  # Use the checker class

                print("Enter new code: ")

                newCode = input()

            # Send newCode to OwnerClass to update master passCode
                master_class.update_mastercode(newCode)
                manageInterface.showMasterUI()  
        
                flag = False

            else:
                error.Error()  # Sending count number to the Error class to check for attempts
    else:
        main.Main(2)
        

