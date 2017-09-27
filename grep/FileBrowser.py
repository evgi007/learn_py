from tkinter import *
from tkinter import filedialog


root =Tk()

root.fileName = filedialog.askopenfilename(filetypes=(("howCode files", ".hc"),("All files","*.*")))

print(root.fileName)