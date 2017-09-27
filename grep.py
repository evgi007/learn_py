import os
import glob
from tkinter import *


root = Tk()
root.title('grep for Windows')
root.geometry('800x200')

scrollbarT_V = Scrollbar(root, orient=VERTICAL)
scrollbarT_H = Scrollbar(root, orient=HORIZONTAL)

T = Text(root, height=2, width=30, yscrollcommand=scrollbarT_V.set, xscrollcommand=scrollbarT_H.set)
T.grid(row=4, columnspan=2, sticky=W+E)
T.insert(END, "Just a text Widget\nin two lines\nJust a text Widget\nin two linesJust a text Widgetin two lines\n")

scrollbarT_V.config(command=T.yview)
scrollbarT_V.grid(row=4, column=2, sticky = N+E)

scrollbarT_H.config(command=T.xview)
scrollbarT_H.grid(row=5, columnspan=2, sticky = W+E)

path_my = StringVar()
pattern_my = StringVar()

path_my.set(os.getcwd())
print(os.getcwd())
# logFileDir = os.chdir("../")
logFileDir = os.path.normpath(os.getcwd() + os.sep + os.pardir)
logFile = os.path.join(logFileDir,'log.txt')


def ls():
    global list_my
    new_path = path_my.get()
    print(os.listdir(new_path))
    list_my = os.listdir(new_path)
    listOfFiles.delete(0, END)
    for index in list_my:
        listOfFiles.insert(END,index)

def SearchPattern():
    ls()
    new_path = path_my.get()
    new_pattern = pattern_my.get()
    open(logFile, 'w').close()
    for index in list_my:
        finalPath = os.path.join(new_path,index)
        if os.path.isfile(finalPath):
            with open(finalPath, 'r') as f:
                data = f.readlines()
                for i, line in enumerate(data):
                    if new_pattern in line:
                        print(finalPath, )
                        print('#'+ str(i+1) + ' ' + line)
                        with open(logFile, 'a') as l:
                            buffer = str(finalPath) + '\n' + '#' + str(i) + ' ' + str(line)
                            l.write(buffer)
        else:
            print ('The path %s if not a file' % finalPath)


scrollbarL_V= Scrollbar(root,orient=VERTICAL)
listOfFiles = Listbox(root, bd=5, width=40, yscrollcommand=scrollbarL_V.set)

scrollbarL_V.config(command=listOfFiles.yview)
scrollbarL_V.grid(column=16, row=0, rowspan=6, sticky = S+N)

scrollbarL_H= Scrollbar(root,orient=HORIZONTAL)
scrollbarL_H.config(command=listOfFiles.xview)
scrollbarL_H.grid(column=10, row=6, columnspan=6, sticky = S+W+E)

listOfFiles.grid(row=0, column=10, columnspan=6, rowspan=9, sticky=N+E)
print(listOfFiles.curselection())

inputLbl = Label(root,text='Folder to search')
inputLbl.grid(row=0,column=0, sticky=N+N)

inputPath = Entry(root, textvariable=path_my, bd=5, width=60)
inputPath.grid(row=0,column=1, columnspan=6, sticky=N+W)

inputLbl = Label(root,text='Pattern to search')
inputLbl.grid(row=1,column=0, sticky=N+W)

inputPattern = Entry(root, textvariable=pattern_my, bd=5, width=20)
inputPattern.grid(row=1, column=1, columnspan=2, sticky=N+W)

searchBtn = Button(root, text='Search', font=12, bd=2, command=SearchPattern)
searchBtn.grid(row=2, column = 4, sticky=N+W)

searchBtn = Button(root, text='ls -> ', font=12, bd=2, command=ls)
searchBtn.grid(row=0, column = 8, padx=3,pady=3, sticky=N)

mainloop()



# if os.path.exists(new_path):
#     print('ok')
#     with open(my_file, 'r') as f:
#         data = f.readlines()
#         print(data[0].strip(),data[1].strip())
#         for line in data:
#             if 'create_socket()' in line:
#                 print (line)
# else:
#     print('Enter correct file path ')

# with open(my_file,'r') as f:
#     data = f.readlines()
#     print(data[0].strip(),data[1].strip())
#     for line in data:
#         if 'create_socket()' in line:
#             print (line)
# with os.scandir(new_path) as it:
#     for entry in it:
#         if not entry.name.startswith('.') and entry.is_file():
#             print(entry.name)

# list_my = glob.glob('*.*')


# logFile = os.path.join(new_path,'log.txt')
# fd = open(logFile,'w')
# fd.truncate()
# fd.close()

# print(glob.glob(str(new_path)+'new_path\*.*'))
# print(glob.glob('*.*'))