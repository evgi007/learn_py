from tkinter import *
# import os

creds='tempfile.temp'

def Signup():
    global nameE
    global pwordE
    global roots

    roots =Tk()
    roots.title('Signup')

    instruction = Label(roots,text='Please entetr new credentials\n')
    instruction.grid(row=0,column=0,sticky=E)

    nameL = Label(roots, text='New Name: ')
    nameL.grid(row=1, column=0, sticky=W)

    pwordL = Label(roots, text='New password: ')
    pwordL.grid(row=2, column=0, sticky=W)

    nameE = Entry(roots)
    pwordE = Entry(roots, show='*')
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)

    signupBtn = Button(roots, text='Signup: ', command=FSSignup)
    signupBtn.grid(row=2, column=0, sticky=W)

    roots.mainloop()

def FSSignup():
    with open(creds,'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

    roots.destroy()
    Login()

def Login():

    rootA = Tk()
    rootA.title('Signup')

    instruction = Label(rootA, text='Please Login\n')
    instruction.grid(row=0, column=0, sticky=E)

    nameL = Label(rootA, text='Username : ')
    nameL.grid(row=1, column=0, sticky=W)

    pwordL = Label(rootA, text='Password: ')
    pwordL.grid(row=2, column=0, sticky=W)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)

    loginBtn = Button(rootA, text='Login: ', command=CheckLogin)
    loginBtn.grid(columnspan=2, sticky=W)

    rmuser = Button(rootA, text='Delete user: ', command=DelUser)
    rmuser.grid(columnspan=2, sticky=W)

    rootA.mainloop()

def CheckLogin():
    with open(creds,'r') as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()