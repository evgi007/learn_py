from tkinter import *

master = Tk()

global index_listee
index_listee = 0

global current
current = 0

listbox = Listbox(master)
listbox.pack()

listbox.insert(END,"a list of items")

def add_new_item():
    global index_listee
    index_listee += 1
    listbox.insert(END, index_listee)

def poll():
    global current
    now = listbox.curselection()
    if now != current:
        print('selection is {%s}', now)
        current = now
    master.after(250, poll)

for items in ['one','two','three','four']:
    listbox.insert(END,items)

b=Button(master,text='Delete',command=lambda listbox=listbox: listbox.delete(ANCHOR))
b.pack()

b2=Button(master,text='Add New',command=add_new_item)
b2.pack()

b3=Button(master,text='Pool',command=poll)
b3.pack()

b4=Button(master,text='Quit',command=quit)
b4.pack()



# class Dialog(Frame):
#     def __init__(self,master):
#         Frame.__init__(self,master)
#         self.list = Listbox(self,selectmode=EXTENDED)
#         self.list.pack(fill=BOTH, expand=1)
#         self.current=0
#         # self.pool()
#
#     def poll(self):
#         now=self.list.curselection()
#         if now != self.current:
#             self.list_has_changed(now)
#             self.current=now
#         self.after(250,self.poll)
#
#     def list_has_changed(self,selection):
#         print('selection is', selection)
#
# da = Dialog(master)

master.mainloop()