from tkinter import *
from tkinter import filedialog

def new_file():
    new = filedialog.askdirectory()

def open():
    open = filedialog.askopenfile()

def save():
    save = filedialog.asksaveasfile()

def saveas():
    save_as = filedialog.asksaveasfilename()

def exit():
    root.destroy()

def undo():
    root.event_generate("<<Undo>>")

def redo():
    root.event_generate("<<Redo>>")

def cut():
    textbox.event_generate("<<Cut>>")

def copy():
    textbox.event_generate("<<Copy>>")

def paste():
    textbox.event_generate("<<Paste>>")

# def font():



root = Tk()
root.geometry("1350x650+5+5")
root.title("Notepad")
root.iconbitmap("notepaddd.ico")

label1 = Label(root,text= "^^^Notepad^^^", bg = "gray")
label1.pack(fill = "x", side = "bottom")

menu = Menu(root)
root.config(menu = menu)

file_menu = Menu(menu,tearoff= FALSE)
menu.add_cascade(label= "File", menu = file_menu)
file_menu.add_command(label = "New File", accelerator = "Ctrl+N",command= new_file)
file_menu.add_command(label = "Open", accelerator = "Ctrl+O",command= open)
file_menu.add_command(label = "Save", accelerator = "Ctrl+S",command= save)
file_menu.add_command(label = "Save As", accelerator = "Ctrl+Shift+S", command= saveas)
file_menu.add_separator() 
file_menu.add_command(label = "Exit",accelerator = "Alt+F4", command = exit)

edit_menu = Menu(menu,tearoff=FALSE)
menu.add_cascade(label= "Edit", menu = edit_menu)
edit_menu.add_cascade(label = "Undo", accelerator = "Ctrl+Z",command=undo)
edit_menu.add_cascade(label = "Redo", accelerator = "Ctrl+Y",command=redo)
edit_menu.add_separator()
edit_menu.add_cascade(label = "Cut", accelerator = "Ctrl+X",command=cut)
edit_menu.add_cascade(label = "Copy", accelerator = "Ctrl+C",command=copy) 
edit_menu.add_cascade(label = "Paste", accelerator = "Ctrl+V",command=paste)
edit_menu.add_separator()
edit_menu.add_cascade(label = "Font", accelerator = "Ctrl+F")

view_menu = Menu(menu,tearoff=FALSE)
menu.add_cascade(label = "View", menu= view_menu)
view_menu.add_cascade(label = "Zoom In",accelerator ="Ctrl+Plus")
view_menu.add_cascade(label = "Zoom Out",accelerator ="Ctrl+Minus")
view_menu.add_separator()
view_menu.add_cascade(label = "Restore Default Zoom",accelerator ="Ctrl+0")

textbox = Text(root,height = 35, width = 200)
textbox.place(x= 0,y = 0)

root.mainloop()