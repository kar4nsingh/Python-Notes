from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator

def translate():
    a= Translator()
    b = a.translate(text = textbox1.get(1.0,END),src= combo1.get(), dest = combo2.get())
    textbox2.delete(1.0,END)
    textbox2.insert(END,b.text)


root = Tk()
root.geometry("1200x600+25+25")
root.config(bg = "orange")
root.resizable(0,0)
root.title("Translator")
root.iconbitmap("translate.ico")



label1 = Label(root,text = "*** Better than Google Translator ***",bg = "skyblue3",font = "12")
label1.pack(fill="x")

frame1 = LabelFrame(root,text = "Input Language", height= "400" , width="525", bg = "pink")
frame1.place(x = 50, y = 50)

frame2 = LabelFrame(root,text = "Output Language", height= "400" , width="525",bg = "pink")
frame2.place(x = 625, y = 50)

label2 = Label(frame1, text = "Select Input Language" , font = " arial 10 bold ", bg = "skyblue3")
label2.place(x = 10 , y = 10)

label3 = Label(frame2, text = "Select Output Language" , font = " arial 10 bold ", bg = "skyblue3")
label3.place(x = 10 , y = 10)

combo1 = ttk.Combobox(frame1, values = list(LANGUAGES.values()), state= "readonly")
combo1.place(x = 200, y = 10)
combo1.set("Choose")

combo2 = ttk.Combobox(frame2, values = list(LANGUAGES.values()), state= "readonly")
combo2.place(x = 200, y = 10)
combo2.set("Choose")

button1 = Button(root, text = "Translate",bg = "red", fg = "white", font = "arial 15 bold", command=translate)
button1.place(x = 550 , y = 500)

textbox1 = Text(frame1, height= 19 , width= 60)
textbox1.place(x = 15 , y = 50)

textbox2 = Text(frame2, height= 19 , width= 60)
textbox2.place(x = 15 , y = 50)

root.mainloop()