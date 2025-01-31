from tkinter import *

root = Tk()
root.geometry("750x500")
root.title("Music Player")
root.resizable(FALSE,FALSE)
root.iconbitmap("music_logo.ico")
# bg = PhotoImage(file = "background1.jpeg")
# limg= Label(root, i=bg)
# limg.pack()

label1 = Label(root,text= "Spotify",font = "arial 14 italic", bg= "green", fg = "black")
label1.pack(fill="x")

# playpause = Image.open("playpause1.png")
# playpause = 

root.mainloop()