# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:51:13 2021

@author: Kris
"""

from Unlock import*
from registerM import*
from Error import*


#this for the interface
def Interface():
    print("Welcome to this house, please enter passcode below: ")
    pw=int(input())
    count = 0

    if(pw==mp): #this master we will take from database 
        print ("Welcome Home " + mn)
        master_I()
    elif(pw==guest_p): # this is for the guest ddatabase
        print ("Welcome to this house" + guest_p)
        guest_p()
    else:
        count +=1
        Error(count)            

#this for a guest
def guest_p():
    pw=int(input())
    count = 0
    if (pw==guest_p()): #this guest_p take from database
        print ("Welcome to this house" + guest_p)
        unlock()
    else:
        count +=1
        Error(count)

#this for a master
def master_I():
    pw=int(input())
    count = 0
    if (pw==master_I):
        print ("Welcome home" + master_I)
        unlock()
    else:
        count +=1
        Error(count)