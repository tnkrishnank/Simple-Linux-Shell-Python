import os

def cmd(l, path):
    original_path = path
    if(len(l) == 1):
        return "/"
    elif(len(l) == 2):
        if(os.path.exists(os.path.join(path, l[1]))):
            if(l[1][0] == "/"):
                return l[1]
            else:
                x = l[1].split('/')
                for i in x:
                    if(i == ".."):
                        path = path[:path.rindex('/')]
                    elif(i == "."):
                        continue
                    else:
                        if(os.path.isdir(os.path.join(path, i))):
                            path = os.path.join(path, i)
                        else:
                            print("cd: Not a directory: " + l[1])
                            return original_path

                if(path[-1] == "/"):
                    path = path[:-1]

                return path
        else:
            print("cd: No such file or directory: " + l[1])
            return original_path
    else:
        print("cd: String not in pwd: " + l[1])
        return original_path