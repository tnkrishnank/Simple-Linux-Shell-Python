import os

def cmd(l, path):
    if(len(l) == 1):
        os._exit(0)
    else:
        print("exit: too many arguments")