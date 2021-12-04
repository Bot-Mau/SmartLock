# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:39:27 2021

@author: kris
"""


import master_class
#this for register the master initially
def Register():
    print("enter master code")
    mastercode = int(input())
    master_class.code_storage(mastercode)
   

