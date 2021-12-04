import Attempt
#import lockdown
#import main

#this for alert
#def Alert(count,password):
    #count += 1
    #trial = 3
    #attempt = trial - count
    
    #if(attempt >0):
     #   print(" You have ", attempt ,"attempt(s) left")
      #  main.Main(count)
        
    #else:
     #   Attempt.Attempts(password)
      #  lockdown.lockdown()
      
def Alert(count,password):
    print(" You have ", count ,"attempt(s) left")
    Attempt.Attempts(count,password)
 
    