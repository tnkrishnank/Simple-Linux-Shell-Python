import os
import stat
import pwd
import grp
from datetime import datetime
from prettytable import PrettyTable

def cmd(l, path):
    columns = ["Inode", "Permission", "Links", "Owner", "Group", "Size", "Last Modified", "Name"]
    table = PrettyTable(columns)
    table.header = False
    table.border = False
    for col in columns:
        table.align[col] = 'r'
    table.align['Name'] = 'l'

    if(len(l) >= 1):
        options = []
        for i in l[1:]:
            if(i[0] == "-"):
                for j in i[1:]:
                    options.append(j)
                l.remove(i)

        if(len(l) == 1):
            l.append(path)

        for i in l[1:]:
            flag = True
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
                                print("ls: cannot access ‘" + i + "': No such file or directory")
                                flag = False
                        else:
                            print("ls: cannot access ‘" + i + "': No such file or directory")
                            flag = False

                if(path[-1] == "/"):
                    path = path[:-1]

            if(flag):
                print(path + ":")
                for i in os.listdir(path):
                    row = ["", "", "", "", "", "", "", ""]
                    flag = False
                    if("a" in options):
                        flag = True
                    elif(i[0] != '.'):
                        flag = True

                    status = os.stat(os.path.join(path, i))
                    if(flag):
                        if("l" in options):
                            time = datetime.fromtimestamp(status.st_mtime).strftime("%B %d %H:%M")
                            row = ["", stat.filemode(status.st_mode), str(status.st_nlink), (pwd.getpwuid(status.st_uid)).pw_name, (grp.getgrgid(status.st_gid)).gr_name, str(status.st_size), time, ""]

                        if("i" in options):
                            row[0] = str(status.st_ino)

                        row[7] = i
                        table.add_row(row)

                print(table)