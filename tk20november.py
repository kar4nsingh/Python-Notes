#DIALOGBOX

from tkinter import *
from tkinter import filedialog

def dialog():
    a = filedialog.askopenfile()

root = Tk()
root.geometry("800x500")

button = Button(root,text = "Click Me",command=dialog)
button.pack(pady = "50")

root.mainloop()