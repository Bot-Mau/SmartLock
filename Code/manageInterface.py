#import checker
#import error
import ownerInterface
import guestInterface
import check_log
import unlock



#All the commands needed to initialize and start the UI for the program 

def showMasterUI():

   # count = 0


        #enteredCode = input("Enter master passcode: ")
        #check = checker.Checker(count,enteredCode)
        
        #if (check == 0):
          print("Do you want to manage?")
          print("1. mastercode")
          print("2. guestcode")
          print("3. see guest checklog")
          print("4. No!!! Just unlock the door")
        #Display all master UI settings and options for master only
          x = int(input())
          print("\n\n\n")
          if (x == 1):
            ownerInterface.changeMasterCode()
            
          elif (x == 2):
              guestInterface.editGuestCode()
            
            
            
            
            #switch(y=int(input()))
            #{
             #case(y=1):
              #   guestInterface.add_guest();
               #  break;
             #case(y=2):
              #   guestInterface.remove_guest();
               #  break;
            #}     
            
            
          elif (x == 3):
            check_log.checklog()
            #showMasterUI()
          else:
            unlock.unlock()


            
        #this for fault option
        #else:
            #error.Error(count,enteredCode)  # Sending count number to the Error class to check for attempts


