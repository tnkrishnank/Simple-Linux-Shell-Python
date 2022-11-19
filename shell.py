import os
import catx
import cdx
import clearx
import cpx
import exitx
import lsx
import mkdirx
import mvx
import pwdx
import rmdirx
import rmx

currentPath = os.getcwd()
while(True):
    try:
        print()
        print(currentPath + "$ ", end="")
        l = input().split()

        if(l[0] == "cat"):
            catx.cmd(l, currentPath)
        elif(l[0] == "cd"):
            currentPath = cdx.cmd(l, currentPath)
        elif(l[0] == "clear"):
            clearx.cmd(l, currentPath)
        elif(l[0] == "cp"):
            cpx.cmd(l, currentPath)
        elif(l[0] == "exit"):
            exitx.cmd(l, currentPath)
        elif(l[0] == "ls"):
            lsx.cmd(l, currentPath)
        elif(l[0] == "mkdir"):
            mkdirx.cmd(l, currentPath)
        elif(l[0] == "mv"):
            mvx.cmd(l, currentPath)
        elif(l[0] == "pwd"):
            pwdx.cmd(l, currentPath)
        elif(l[0] == "rmdir"):
            currentPath = rmdirx.cmd(l, currentPath)
        elif(l[0] == "rm"):
            currentPath = rmx.cmd(l, currentPath)
        else:
            print(l[0] + ": command not found")
    except KeyboardInterrupt:
        print()
        exitx.cmd(["exit"], currentPath)
    except:
        continue
