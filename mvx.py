import os
import shutil

def cmd(l, path):
    original_path = path
    source_path = ""
    destination_path = ""
    if(len(l) >= 3):
        options = []
        for i in l[1:]:
            if(i[0] == "-"):
                for j in i[1:]:
                    options.append(j)
                l.remove(i)

        c = 0
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
                        if(os.path.exists(os.path.join(path, j))):
                            if(os.path.isdir(os.path.join(path, j))):
                                path = os.path.join(path, j)
                            else:
                                print("mv: cannot create directory '" + l[2] + "': No such file or directory")
                                flag = False
                        else:
                            print("mv: cannot create directory '" + l[2] + "': No such file or directory")
                            flag = False

                if(path[-1] == "/"):
                    path = path[:-1]

                if(c == 0):
                    source_path = os.path.join(path, x[-1])
                else:
                    destination_path = os.path.join(path, x[-1])

                c = c + 1

        if(flag):
            if(os.path.exists(source_path)):
                if(os.path.isfile(source_path)):
                    if(os.path.exists(destination_path)):
                        if(os.path.isfile(destination_path)):
                            source = open(source_path, "r")
                            destination = open(destination_path, "w")
                            destination.write(source.read())
                            destination.close()
                            source.close()
                            os.remove(source_path)
                        else:
                            source = open(source_path, "r")
                            destination = open(destination_path + source_path[source_path.rindex('/'):], "w")
                            destination.write(source.read())
                            destination.close()
                            source.close()
                            os.remove(source_path)
                    else:
                        source = open(source_path, "r")
                        destination = open(destination_path, "w")
                        destination.write(source.read())
                        destination.close()
                        source.close()
                        os.remove(source_path)
                elif(os.path.isdir(source_path)):
                    if("r" in options):
                        if(os.path.exists(destination_path)):
                            if(os.path.isfile(destination_path)):
                                print("mv: cannot overwrite non-directory '" + l[2] + "' with directory '" + l[1] + "'")
                            else:
                                shutil.copytree(source_path, destination_path + "/" + source_path[source_path.rindex('/'):])
                                shutil.rmtree(source_path)
                        else:
                            shutil.copytree(source_path, destination_path + "/" + source_path[source_path.rindex('/'):]) 
                            shutil.rmtree(source_path)
                    else:
                        print("mv: -r not specified; omitting directory '" + l[1] + "'")
            else:
                print("mv: cannot stat '" + l[1] + "': No such file or directory")
    elif(len(l) == 2):
        print("mv: missing destination file operand after '" + l[1] + "'")
    elif(len(l) == 1):
        print("mv: missing file operand")
    else:
        print("mv: target '" + l[-1] + "' is not a directory")