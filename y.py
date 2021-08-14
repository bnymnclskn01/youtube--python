from tkinter import*
from tkinter import messagebox
pencere =Tk()
pencere.title("Ders Örneği")
pencere.geometry("320x300")
uygulama=Frame(pencere)
uygulama.grid()
"""
L1=Label(uygulama,text="İfade Girin")
L1.grid(padx=110,pady=10)
E1=Entry(uygulama,bd=2)
E1.grid(padx=100,pady=3)
pencere.mainloop()
"""
lb1=Listbox(uygulama)
lb1.insert(1,"İstanbul")
lb1.insert(2,"Ankara")
lb1.insert(3,"Kars")
lb1.insert(4,"İzmir")
lb1.insert(5,"Hakkari")
lb1.grid(padx=110,pady=10)
pencere.mainloop()
txt1=Text