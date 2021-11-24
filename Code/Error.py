# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:47:20 2021

@author: kris
"""
from Unlock import*
from registerM import*


#this for the error part for master 
def Error(count):
    print("You have input the wrong passcode")
    attempts = 3 - count #this is counting number of trial 

    if (count < 3 ):  
        print(" You have" + attempts +"left" )
        save_log()
    else:
        lockdown()
            
        

