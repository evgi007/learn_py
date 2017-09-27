from tkinter import *
from tkinter import ttk

# master = Tk()
master = Frame()
master.grid()
# master.create_widgets()


display = Entry(master,bd=1,bg='powder blue')
display.grid(row=1, sticky=E)

label1 = Label(master, text='Enter value:')
label1.grid(row=1, sticky=W)

checkbutton = Checkbutton(master)
checkbutton.grid(row=2)

# Create scroll bar
scrollbar_V = Scrollbar(master);
scrollbar_H = Scrollbar(master, orient=HORIZONTAL);
scrollbar_V.grid(row=2,column=5, sticky =N+S+W )
scrollbar_H.grid(row=5,column=4, sticky =N+S+E+W )

def select_item(event):
    w= event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    var.Entry.set(value)

def add_symbol():
    to_add =var.Entry.get()
    listbox1.insert('end', to_add)

# Create listbox widget
listbox1 = Listbox(master,font=('',12), width=15, height=10, yscrollcommand=scrollbar_V.set, xscrollcommand=scrollbar_H.set)
listbox1.bind('<<ListBoxSelect>>', select_item)
# listbox1.insert(1, 'EVIL')
# listbox1.insert(2,'SBUX')
listbox1.grid(row=2,column=4)

evil_corp = ['EVIL','Cran','SBUX','EVIL1','Cran1','SBUX3','EVIL2','Cran2','SBUX2','EVIL2','Cran2','SBUX2','all countries that do not']

for evil in evil_corp:
    listbox1.insert('end',evil)


scrollbar_V.config(command=listbox1.yview)
scrollbar_H.config(command=listbox1.xview)

listbox1.itemconfig(0,{'bg':'red','fg':'white'})
listbox1.itemconfig(2,{'fg':'blue'})

mainloop()
