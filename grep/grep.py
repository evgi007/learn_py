import os
import codecs
from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('grep for Windows')
root.geometry('1100x200')

path_my = StringVar()
pattern_my = StringVar()

choosen_file = StringVar()
choosen_directory = StringVar()

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

def browse_files():
    root.fileName = filedialog.askopenfilename(filetypes=(("howCode files", ".hc"), ("All files", "*.*")))
    print(root.fileName)
    choosen_file.set(root.fileName)

def browse_directory():
    root.FolderName = filedialog.askdirectory()
    print(root.FolderName)
    choosen_directory.set(root.FolderName)


def SearchPattern():
    ls()

    new_path = path_my.get()

    new_pattern = pattern_my.get()
    open(logFile, 'w').close()

    for index in list_my:
        finalPath = os.path.join(new_path,index)
        print(finalPath)

        if os.path.isfile(finalPath):
            with codecs.open(finalPath, 'r', encoding="ISO-8859-1") as f:
                data = f.readlines()
                for i, line in enumerate(data):

                    if str(new_pattern) in line:

                        print(finalPath, )
                        print('#'+ str(i+1) + ' ' + line)
                        with open(logFile, 'a') as l:
                            buffer = str(finalPath) + '\n' + '#' + str(i) + ' ' + str(line)
                            l.write(str(finalPath))
        else:
            print ('The path %s if not a file' % finalPath)

listOfFiles = Listbox(root, bd=5, width=40)
listOfFiles.grid(row=0, column=10, columnspan=6, rowspan=9, sticky=N+E)

inputLbl = Label(root,text='Folder to search')
inputLbl.grid(row=0,column=0, sticky=N+W)

inputPath = Entry(root, textvariable=path_my, bd=5, width=60)
inputPath.grid(row=0,column=1, columnspan=6, sticky=N+W)

inputLbl = Label(root,text='Pattern to search')
inputLbl.grid(row=1,column=0, sticky=N+W)

inputPattern = Entry(root, textvariable=pattern_my, bd=5, width=20)
inputPattern.grid(row=1, column=1, columnspan=2, sticky=N+W)

searchBtn = Button(root, text='Search...', font=12, bd=2, command=SearchPattern)
searchBtn.grid(row=2, column = 4, sticky=N+W)

searchBtn = Button(root, text='ls -> ', font=12, bd=2, command=ls)
searchBtn.grid(row=0, column = 8, padx=3,pady=3, sticky=N)

BrowseFileBtn = Button(root, text='Choose file: ', font=12, bd=2, command=browse_files)
BrowseFileBtn.grid(row=3, column = 0, padx=3,pady=3, sticky=W)

inputFileName = Entry(root, textvariable=choosen_file, bd=5, width=60)
inputFileName.grid(row=3,column=1, columnspan=6, sticky=W)

BrowseDirectoryBtn = Button(root, text='Choose Directory: ', font=12, bd=2, command=browse_directory)
BrowseDirectoryBtn.grid(row=4, column = 0, padx=3,pady=3, sticky=W)


inputDirectoryName = Entry(root, textvariable=choosen_directory, bd=5, width=60)
inputDirectoryName.grid(row=4,column=1, columnspan=6, sticky=W)

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