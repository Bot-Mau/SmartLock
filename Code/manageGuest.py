def addGuestCode:
      
  flag = True
  
  print("Adding guest code...\n)
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Enter new guest code: )
      
      flag = False
     
     else
      
      print("Incorrect code...\n")
  

def changeGuestCode:
    
  flag = True
            
  print("Changing guest code...\n)
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Enter new guest code: ")
    
      newCode = string(input())
    
      #Send newCode to OwnerClass to update guest passcode
      
      flag = False
     
     else
      
      print("Incorrect code\n")
    
def addGuestName:
    
  flag = True
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Enter new guest name: ")
    
      newName = string(input())
    
      #Send newName to logs to add the guest name
      
      flag = False
     
     else
      
      print("Incorrect code\n")
  
def removeGuestName:
    
  flag = True
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Enter guest name: ")
    
      newName = string(input())
    
      #Send newName to logs to remove the guest name
      
      flag = False
     
     else
      
      print("Incorrect code\n")
      
def editGuestName:
      
  flag = True
  
  while(flag):
  
    if(compareMasterCode(enteredCode)): # Use the checker class 
    
      print("Editing Guest Name\n")
      
      removeGuestName()
      
      addGuestName()
      
      flag = False
     
     else
      
      print("Incorrect code\n")
  
