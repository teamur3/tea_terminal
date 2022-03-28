#!/bin/python3
from os import *
from core import *

cycle = True
ver = "0.0.4-2022" 

print ("Welcome!")

while cycle == True:
    try:
        p = getcwd()
    except IOError:
        p = "/io-error/"

    try:
        i = input(p + ">")
        c, i1 = i.split()
        i = c.upper()
    except ValueError:
        i = i.strip()
        c = i
        i = i.upper()
        i1 = "."
        i2 = " "
    except EOFError: pass

    if i == "": pass

    elif i == "CD": 
        cd(i1)

    elif i == "LD":
        ld(i1)

    elif i == "VER":
        print ("TeaTerminal version " + ver)

    elif i == "SYSTEM":
        system(i1)
        
    elif i == "CAL":
        cal(i1)
        
    elif i == "EXIT":
        cycle = False
    
    else:
        print (c + " - command not found!")