from tkinter import *
from functools import partial
def validatelogin(username,password):
    print("Lütfen Kullanıcı Adını Giriniz : ",username.get())
    print("Lütfen Kullanıcı Şifre Giriniz : ",password.get())
tkWindow= Tk()
tkWindow.geometry("400x150")
tkWindow.title("Yazamayanlar Giriş Yap - Instagram= Mekasoftech")
UsernameLabel=Label(tkWindow,text="Username").grid(row=0, column=0)
Username=StringVar()
UsernameEntry=Entry(tkWindow,textvariable=Username).grid(row=0,column=1)

PasswordLabel=Label(tkWindow,text="Password").grid(row=1, column=0)
Password=StringVar()
PasswordEntry=Entry(tkWindow,textvariable=Password).grid(row=1,column=1)

validatelogin=partial(validatelogin,Username,Password)
LoginButton=Button(tkWindow, text="Login", command=validatelogin).grid(row=4,column=0)
tkWindow.mainloop()