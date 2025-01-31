from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("800x500+20+20")
root.title("Hello")
root.config(bg = "blue")
x = Label(root, text = "ComboBox", font = "arial 30 italic", bg = "blue", fg = "white")
x.pack()

#COMBOBOX

combo = ttk.Combobox(root, textvariable = StringVar(), values = ["Male", "Female" , "Others", "LGBTQ+"])
combo["state"] = "readonly"
combo.set("Select your Gender")
# combo.current(0)
combo.place(x = 50, y = 60)

#SPINBOX

spin = Spinbox(root, textvariable= StringVar(),values = ["Male", "Female" , "Others", "LGBTQ+"] , state = "readonly")
spin.place(x = 50, y = 120)

root.mainloop()