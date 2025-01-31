from tkinter import *
root = Tk()
root.geometry("500x600")
root.title("Desktop")
root.config(bg = "violet")

label = Label(root,text = "Heyyyy" , font = ("arial", 40 , "italic"), bg = "blue", fg = "black")
label.pack(fill = "x")

label = Label(root,text = "Hello" , font = ("arial", 40 , "bold"), bg = "blue", fg = "black")
label.place(x = 300,y = 150)

# label = Label(root,text = "hi" , font = ("arial", 40 , "italic"), bg = "blue", fg = "black")
# label.grid(padx = 50)

root.mainloop()