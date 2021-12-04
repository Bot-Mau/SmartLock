#this is for the master class storage
def code_storage(a):
    code = str(a)
    f = open("master.txt", "a")
    f.write("Mastercode : " + code + '\n')    
    f.close()
    
def update_mastercode(a):
    code = str(a)
    f = open("master.txt", "r")
    list_of_lines= f.readlines()
    list_of_lines[0] = "Mastercode : " + code + '\n'
    
    f = open("master.txt", "w")
    f.writelines(list_of_lines)
    f.close()
    
def mastercode():
    f = open ("master.txt", "r")
    wordlist = [line.split() for line in f]
   
    return(wordlist[0][2])