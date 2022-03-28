from os import *

def ioe(): 
    print ("IO-error")
    
def cd(path):
    try: 
        chdir(path)
    except IOError:
        ioe()
        
def ld(path):
    try:
        print("[..]\n" + str(listdir(path=path)))
    except IOError:
        ioe()
        
def cal(p):
    try:
        print(eval(p))
    except SyntaxError:
        print ("Unexcepted error")
    except ZeroDivisionError:
        print ("Error: you can't divide by zero.")
    