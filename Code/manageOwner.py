def changeMasterCode:
  
  flag = True
  
  count = 0
  
  print("Changing master passcode...\n")
  
  while(flag):
  
    if(compareMastercode(enteredCode)): # Use the checker class 
    
      print("Enter new code: ")
    
      newCode = string(input())
    
      #Send newCode to OwnerClass to update master passCode
      
      flag = False
     
     else:
      
      print("Incorrect passcode...\n")
      
      count += 1
      
      Error(count)        # Sending count number to the Error class to check for attempts
    
def editName:
  
  flag = True
  
  count = 0
  
  print("Changing master name...\n")
  
  while(flag):
  
    if(compareMastercode(enteredCode)): # Use the checker class 
    
      print("Enter new name: ")
    
      newName = string(input())
    
      #Send newCode to OwnerClass to update master passCode
      
      flag = False
     
     else:
      
      print("Incorrect passcode...\n")
      
      count += 1
      
      Error(count)        # Sending count number to the Error class to check for attempts
