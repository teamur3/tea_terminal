#!/bin/python3
from os import *

cycle = True
ver = "0.0.3-2022" 

def ioe(): 
    print ("IO-error")


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
        try: 
           chdir(i1)
        except IOError:
            ioe()

    elif i == "LD":
        try:
            print("[..]\n" + str(listdir(path=i1)))
        except IOError:
            ioe()

    elif i == "VER":
        print ("TeaTerminal version " + ver)

    elif i == "EXIT":
        cycle = False

    elif i == "SYSTEM":
        system(i1)
        
    elif i == "CAL":
        try:
            print(eval(i1))
        except SyntaxError:
            print ("Unexcepted error")
        except ZeroDivisionError:
            print ("Error: you can't divide by zero.")
    
    else:
        print (c + " - command not found!")