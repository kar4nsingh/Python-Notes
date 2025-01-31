from tkinter import *
from tkinter import messagebox

def submit():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    d = entry4.get()
    textbox.delete(END)
    textbox.insert(END,f"\nName : {a}\n")
    textbox.insert(END,f"Roll No. : {b}\n")
    textbox.insert(END,f"Phone Number : {c}\n")
    textbox.insert(END,f"Address : {d}")
    messagebox.showinfo("Success", "Transfer Success")

def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    textbox.delete(1.0,END)
   

def exit():
    root.destroy()

root = Tk()
root.geometry("800x550")
root.title("Excellence")
root.config(bg = "red")
root.iconbitmap("mars.ico")
root.resizable(False,False)

headline = Label(root,text = "Python", font = ("calibri", 16 , "bold") , bg = "gold")
headline.pack(fill = "x")

frame1 = Frame(root,height = 300, width = 300 , bg = "yellow")
frame1.place(x = 70, y = 70)

frame3 = LabelFrame(root ,text = "receipt" ,  height= 300, width = 300 , bg = "yellow")
frame3.place(x = 400, y = 70)

frame4 = Frame(root, height = 100 , width = 630 , bg = "yellow")
frame4.place(x = 70, y = 400)

textbox = Text(frame3 , height = 17.3 , width = 37)
textbox.pack()

name = Label(frame1, text = "Student's Name : ", font = ("calibri", 12 , "bold"), bg = "yellow")
name.place(x = 10, y = 10)
entry1 = Entry(frame1,)
entry1.place(x = 80,y = 40)

rollno = Label(frame1, text = "Roll No. : ", font = ("calibri", 12 , "bold"), bg = "yellow")
rollno.place(x = 10, y = 70)
entry2 = Entry(frame1,)
entry2.place(x = 80,y = 100)

phone = Label(frame1, text = "Phone Number : ", font = ("calibri", 12 , "bold"), bg = "yellow")
phone.place(x = 10, y = 130)
entry3 = Entry(frame1,)
entry3.place(x = 80,y = 160)

address = Label(frame1, text = "Address : ", font = ("calibri", 12 , "bold"), bg = "yellow")
address.place(x = 10, y = 190)
entry4 = Entry(frame1,)
entry4.place(x = 80,y = 220)

submit = Button(frame4,text = "SUBMIT", font = "calibri 16 bold" , bg = "red" , fg = "gold", command= submit , cursor= "hand2")
submit.place(x = 50 , y = 25)

clear = Button(frame4,text = "CLEAR", font = "calibri 16 bold" , bg = "red" , fg = "gold", command= clear , cursor= "hand2")
clear.place(x = 280 , y = 25)

exit = Button(frame4,text = "EXIT", font = "calibri 16 bold" , bg = "red" , fg = "gold", command= exit , cursor= "hand2")
exit.place(x = 500 , y = 25)

root.mainloop()