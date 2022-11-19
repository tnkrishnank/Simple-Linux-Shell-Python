import os

def cmd(l, path):
    original_path = path
    if(len(l) > 1):
        options = []
        for i in l[1:]:
            if(i[0] == "-"):
                for j in i[1:]:
                    options.append(j)
                l.remove(i)

        for i in l[1:]:
            flag = True
            path = original_path
            if(i[0] == "/"):
                path = i
            else:
                x = i.split('/')
                for j in x[:-1]:
                    if(j == ".."):
                        path = path[:path.rindex('/')]
                    elif(j == "."):
                        continue
                    else:
                        if('p' not in options):
                            if(os.path.exists(os.path.join(path, j))):
                                if(os.path.isdir(os.path.join(path, j))):
                                    path = os.path.join(path, j)
                                else:
                                    print("mkdir: cannot create directory ‘" + i + "': No such file or directory")
                                    flag = False
                            else:
                                print("mkdir: cannot create directory ‘" + i + "': No such file or directory")
                                flag = False
                        else:
                            path = os.path.join(path, j)

                if(path[-1] == "/"):
                    path = path[:-1]

                path = os.path.join(path, x[-1])

            if(flag):
                if(not os.path.exists(path)):
                    if('p' in options):
                        os.makedirs(path)
                    else:
                        os.mkdir(path)
                else:
                    print("mkdir: cannot create directory ‘" + i + "’: File exists")