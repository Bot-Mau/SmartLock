def addGuestCode:
      
  flag = True

  count = 0
  
  print("Adding guest code...\n)
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Enter new guest code: )
      
      flag = False
     
     else:
      
      print("Incorrect passcode...\n")
      
      count += 1
      
      Error(count)        # Sending count number to the Error class to check for attempts

def changeGuestCode:
    
  flag = True
            
  count = 0
            
  print("Changing guest code...\n)
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Enter new guest code: ")
    
      newCode = string(input())
    
      #Send newCode to OwnerClass to update guest passcode
      
      flag = False
     
     else:
      
      print("Incorrect passcode...\n")
      
      count += 1
      
      Error(count)        # Sending count number to the Error class to check for attempts
    
def addGuestName:
    
  flag = True
        
  count = 0
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Enter new guest name: ")
    
      newName = string(input())
    
      #Send newName to logs to add the guest name
      
      flag = False
     
     else:
      
      print("Incorrect passcode...\n")
      
      count += 1
      
      Error(count)        # Sending count number to the Error class to check for attempts
  
def removeGuestName:
    
  flag = True
        
  count = 0
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Enter guest name: ")
    
      newName = string(input())
    
      #Send newName to logs to remove the guest name
      
      flag = False
     
     else:
      
      print("Incorrect passcode...\n")
      
      count += 1
      
      Error(count)        # Sending count number to the Error class to check for attempts
      
def editGuestName:
      
  flag = True
        
  count = 0 
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Editing Guest Name\n")
      
      removeGuestName()
      
      addGuestName()
      
      flag = False
     
     else:
      
      print("Incorrect passcode...\n")
      
      count += 1
      
      Error(count)        # Sending count number to the Error class to check for attempts
