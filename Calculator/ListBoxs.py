# from tkinter import *
from ClassDialog import *

master = Tk()

da = Dialog(master)

b=Button(master,text='Delete',command=da.delete_item)
b.pack()

b2=Button(master,text='Add New',command=da.add_new_item)
b2.pack()

b4=Button(master,text='Quit',command=quit)
b4.pack()



master.mainloop()