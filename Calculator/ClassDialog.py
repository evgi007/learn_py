from tkinter import *

class Dialog(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.list = Listbox(master,selectmode=EXTENDED)
        self.list.pack(fill=BOTH, expand=1)
        self.current=0
        self.index_listee=0
        self.list.insert(END, "a list of items")

        for items in ['one', 'two', 'three', 'four']:
            self.list.insert(END,items)

        self.pool_constantly()

    def pool_constantly(self):
        now=self.list.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current=now
        self.after(250,self.pool_constantly)

    def list_has_changed(self,selection):
        print('selection is', selection)

    def add_new_item(self):
        self.index_listee += 1
        self.list.insert(END, self.index_listee)

    def delete_item(self):
        self.list.delete(ANCHOR)