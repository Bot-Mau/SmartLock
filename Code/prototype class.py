# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 20:13:50 2021

@author: drago

attempt entity class
"""

# import important module
from datetime import datetime, date


def get_time():
        now = datetime.now()
        
        current_time = now.strftime("%H:%M:%S")
        return(current_time)

def get_date():
    today = date.today()
    
    current_date = today.strftime("%m/%d/%Y")
    return (current_date)
"""
prot type code to use for data storage, can be used for storing infromation
can be used to access varibales between functions.
"""
def log(a):
    code = str(a)
    f = open("log.txt", "a")
    f.write("code : " + code + '\n')
    f.write("time : "  + get_time() + '\n')
    f.write("date : " + get_date()+ '\n')
    f.close()
    
def read_log():
    f= open("log.txt", "r")
    print(f.read())
    f.close()

def code():
    wordlist = []
    f = open ("log.txt", "r")
    wordlist = [line.split() for line in f]
   
    print(wordlist)
    print(wordlist[0][2])

"""
master class storage
"""
def code_storge(a):
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