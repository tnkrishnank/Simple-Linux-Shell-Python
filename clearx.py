import os

def cmd(l, path):
    if(len(l) == 1):
        os.system("clear")
    else:
        print("clear: too many arguments")