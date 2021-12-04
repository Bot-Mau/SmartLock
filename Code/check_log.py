#this is check log 
  
def checklog():
    f= open("log.txt", "r")
    print(f.read())
    f.close()