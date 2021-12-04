#import Register_m
#import master_class
import interface
import checker
import manageInterface
import error
#import alert
#import Attempt
import unlock

 
count = 2

def Main(count):#interface
    password = interface.Interface()
    check = checker.Checker(count,password)
    if (check == 0):
        manageInterface.showMasterUI()
        #unlock.unlock()
        print("\n\n\n")
        Main(count)
        
    elif (check == 1):
        unlock.unlock()
        
    else:
        #password = 
        error.Error(count,password)
        
        
        Main(count)
        