from tkinter import *

def button():
    x = user.get()
    y = passw.get()
    print(x,y)

def forgot():
    print("otp on mobile number")

root = Tk()
root.geometry("1000x500")
root.title("Tinder Login")
root.config(bg ="orange")

username = Label(root,text = "Username",font = ("arial",16, "bold"),bg = "cyan")
username.pack()
user = Entry(root,font = ("arial", 16,"bold"))
user.pack(padx = 5, pady = 5)

# username = Label(root,text = "Username",font = ("arial",16, "bold"),bg = "cyan")
# username.place(x = 40, y = 70)
# user = Entry(root,font = ("arial", 16,"bold"))
# user.place(x = 40, y = 110)

# username = Label(root,text = "Username",font = ("arial", 16, "bold"),bg = "cyan")
# username.grid(row = 0, column= 5)
# user = Entry(root,font = ("arial", 16, "bold"))
# user.grid(row = 0, column= 6)

password = Label(root,text = "Password",font = ("arial",16, "bold"),bg = "cyan")
password.pack()
passw = Entry(root,font = ("arial", 16,"bold"), show = ("*"))
passw.pack(padx = 5, pady = 5)

# password = Label(root,text = "Password",font = ("arial",16, "bold"),bg = "cyan")
# password.place(x = 40, y = 160)
# passw = Entry(root,font = ("arial", 16,"bold"), show = ("*"))
# passw.place(x = 40, y = 200)

# password = Label(root,text = "Password",font = ("arial",16 , "bold"),bg = "cyan")
# password.grid(row = 1 , column = 5)
# passw = Entry(root,font = ("arial", 16,"bold"), show = ("*"))
# passw.grid(row = 1 , column= 6)

but = Button(root,text = "Login",font = ("arial", 16,"bold"), bg = "red" , command = button , cursor= "hand2")
but.pack(padx = 5, pady = 5)
buttt = Button(root,text = "Forgot Password",font = ("arial", 16,"bold"), bg = "red" , cursor= "hand2", command = forgot)
buttt.pack(padx = 5, pady = 5)

# but = Button(root,text = "Login",font = ("arial", 16,"bold"), bg = "red" , command = button , cursor= "hand2")
# but.place(x = 500, y = 100)
# buttt = Button(root,text = "Forgot Password",font = ("arial", 16,"bold"), bg = "red" , cursor= "hand2", command = forgot)
# buttt.place(x = 500, y = 150)

# but = Button(root,text = "Login",font = ("arial", 16,"bold"), bg = "red" , command = button , cursor= "hand2")
# but.grid(row = 2 , column = 5)
# buttt = Button(root,text = "Forgot Password",font = ("arial", 16,"bold"), bg = "red" , cursor= "hand2", command = forgot)
# buttt.grid(row = 3, padx = 50,pady = 20, columnspan = 2 )

root.mainloop() 