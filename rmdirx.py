import os
import shutil

def cmd(l, path):
    original_path = path
    flag_path = False
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
                for j in x:
                    if(j == ".."):
                        path = path[:path.rindex('/')]
                    elif(j == "."):
                        continue
                    else:
                        if(os.path.exists(os.path.join(path, j))):
                            if(os.path.isdir(os.path.join(path, j))):
                                path = os.path.join(path, j)
                            else:
                                print("rmdir: cannot remove '" + i + "': Is a file")
                                flag = False
                        else:
                            print("rmdir: cannot remove '" + i + "': No such file or directory")
                            flag = False

                if(path[-1] == "/"):
                    path = path[:-1]

            if(flag):
                shutil.rmtree(path)
                if(original_path == path):
                    flag_path = True

        if(flag_path):
            return original_path[:original_path.rindex('/')]
        else:
            return original_path
    else:
        return original_path