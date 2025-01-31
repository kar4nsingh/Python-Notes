from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as mysql

def insert_data(name,classs,subject,gender,country,state,contact,message):
    connection = mysql.connect(
        host = "localhost",
        user = "root",
        password = "412001",
        database = "registration_form"
    )

    cursor = connection.cursor()
    query = """INSERT INTO ENTRIES (NAME,CLASS,SUBJECT,GENDER,COUNTRY,STATE,CONTACT,MESSAGE)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    data_tuple = (name,classs,subject,gender,country,state,contact,message)
    cursor.execute(query,data_tuple)
    connection.commit()
    connection.close()
    cursor.close()


root = Tk()
root.geometry("800x550+50+50")
root.config(bg="silver")
root.resizable(0,0)

def submit():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()
    d = entry4.get()
    e = entry5.get()
    f = entry6.get()
    g = entry7.get()
    h = entry8.get(1.0, END)

    insert_data(a,b,c,d,e,f,g,h)
    if a =="" or b =="" or c =="" or d == "choose your gender" or e == "choose your country" or f == "" or g == "" or h == "" :
        messagebox.showerror("Error","All fields are required !")

    else:
        textbox.delete(END)
        textbox.insert(END,f"\nName : {a}\n")
        textbox.insert(END,f"Class : {b}\n")
        textbox.insert(END,f"Subject : {c}\n")
        textbox.insert(END,f"Gender : {d}\n")
        textbox.insert(END,f"Country : {e}\n")
        textbox.insert(END,f"State : {f}\n")
        textbox.insert(END,f"Contact No. : {g}\n")
        textbox.insert(END,f"Message : {h}")
        messagebox.showinfo("Success", "Transfer Success !")

def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.set("choose your gender")
    entry5.set("choose your country")
    # entry6.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(1.0,END)
    textbox.delete(1.0,END)
    messagebox.showinfo("Clear","Clear Success !")

def exit():
    root.destroy()

label1 = Label(root, text = "Entryyyy", font = "arial 12 bold",bg = "blue")
label1.pack(fill = "x")

frame1 = Frame(root, height = 400, width =400, bg = "skyblue1")
frame1.place(x = 10, y = 30)

frame2 = LabelFrame(root, text = "receipt" , height = 400, width = 370, bg = "skyblue1")
frame2.place(x = 420, y = 30)

frame3 = Frame(root,height = 80 , width = 780 , bg = "skyblue1")
frame3.place(x = 10 , y = 450)

textbox = Text(frame2 , height = 24 , width = 45)
textbox.pack()

name = Label(frame1, text = "Name :", font = "arial 10 bold" , bg = "skyblue1")
name.place(x = 5 , y = 10)

classs = Label(frame1, text = "Class :", font = "arial 10 bold", bg = "skyblue1")
classs.place(x = 5 , y = 40)

subject = Label(frame1, text = "Subject :", font = "arial 10 bold", bg = "skyblue1")
subject.place(x = 5, y = 70)

gender = Label(frame1, text = "Gender :", font = "arial 10 bold", bg = "skyblue1")
gender.place(x = 5, y = 100)

country = Label(frame1, text = "Country :", font = "arial 10 bold", bg = "skyblue1")
country.place(x = 5, y = 130)

state = Label(frame1, text = "State :", font = "arial 10 bold", bg = "skyblue1")
state.place(x = 5, y = 160)

contact = Label(frame1, text = "Contact No.:", font = "arial 10 bold", bg = "skyblue1")
contact.place(x = 5, y = 190)

messagee = Label(frame1, text = "Message :", font = "arial 10 bold", bg = "skyblue1")
messagee.place(x = 5, y = 220)

entry1 = Entry(frame1)
entry1.place(x = 150 , y = 12)

entry2 = Entry(frame1)
entry2.place(x = 150 , y = 42)

entry3 = Entry(frame1)
entry3.place(x = 150 , y = 72)

entry4 = ttk.Combobox(frame1, values= ("Male", "Female", "Others"), state= "readonly")
entry4.set("choose your gender")
entry4.place(x = 150 , y = 102)

entry5 = ttk.Combobox(frame1, values= ("India", "USA", "Others"), state= "readonly")
entry5.place(x = 150 , y = 132)
entry5.set("choose your country")

entry6 = Spinbox(frame1, values= ("Punjab", "Himachal","UP", "Others"),state = "readonly")
entry6.place(x = 150 , y = 162)

entry7 = Entry(frame1)
entry7.place(x = 150 , y = 192)

entry8 = Text(frame1 , height= 7 , width = 47)
entry8.place(x = 10, y = 255)

#frame3

submit = Button(frame3, text = "SUBMIT", width = 10 , font = "arial 13 bold" , bg = "blue" , fg = "white" , cursor= "hand1", command= submit)
submit.place(x = 50, y = 23)

clear = Button(frame3, text = "CLEAR", width = 10 , font = "arial 13 bold", bg = "blue" , fg = "white", cursor= "hand1",command = clear)
clear.place(x = 350, y = 23)

exit = Button(frame3, text = "EXIT", width = 10 , font = "arial 13 bold", bg = "blue" , fg = "white", cursor= "hand1", command= exit)
exit.place(x = 600, y = 23)

root.mainloop()