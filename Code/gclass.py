#this is for the guest class storage
def add_guest():
    
    name = input("Enter guest name: ")
    passcode = str(input("Enter passcode for Guestnames " + name + ": "))
    f = open ("guest.txt" , 'a')
    f.write("Guestnames : " + name + " code : " + passcode + ' \n')
    
def remove_guest():
    f = open ("guest.txt", 'r')
    name = input("What guest name do u wish to delete \n")
    wordlist = [line.split() for line in f]
    f.seek(0,0)
    lines = f.readlines()
    f.close()
    
    for x in range(len(wordlist)):
        if wordlist[x][2] == name:
            del lines[x]
            
    f = open ("guest.txt", "w+")
    for line in lines:
        f.write(line)
    f.close()

#def update_guestcode(a):
    #code = str(a)
   # f = open("guest.txt", "r")
    #list_of_lines= f.readlines()
    #list_of_lines[0] = "Guestcode : " + code + '\n'
    
    #f = open("guest.txt", "w")
    #f.writelines(list_of_lines)
    #f.close()
    
def guestcode():
    f = open ("guest.txt", "r")
    wordlist = [line.split() for line in f]
    passcode = []
    
    for x in range(len(wordlist)):
        passcode.append(wordlist[x][5])
    
    return(passcode)

#def sosanh():
   # x = guestcode()
   # y = str(345)
   # for i in x:
    #    if  y == i:
     #       print('done')
      #  else:
       #     print('f')
            
