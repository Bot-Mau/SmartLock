def changeMasterCode:
  
  flag = True
  
  print("Changing master passcode...\n")
  
  while(flag):
  
    if(compareMastercode(enteredCode)): # Use the checker class 
    
      print("Enter new code: ")
    
      newCode = string(input())
    
      #Send newCode to OwnerClass to update master passCode
      
      flag = False
     
     else
      
      print("Incorrect code...\n")
    
def editName:
  
  flag = True
  
  print("Changing master name...\n")
  
  while(flag):
  
    if(compareMastercode(enteredCode)): # Use the checker class 
    
      print("Enter new name: ")
    
      newName = string(input())
    
      #Send newCode to OwnerClass to update master passCode
      
      flag = False
     
     else
      
      print("Incorrect code...\n")
