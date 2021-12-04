#this for the checker
import master_class
import gclass
#import manageInterface
import unlock
#import error


def Checker(count,password):
    password = str(password)
    if(password == master_class.mastercode()): 
        #manageInterface.showMasterUI()
        unlock.unlock()
        return(0)
    
    else:
        x = gclass.guestcode()
        for i in x:
            if  password == i:
                return(1)
            
                #return(1)
            #else:
                #error.Error(count,password)
    return(2)
    
        