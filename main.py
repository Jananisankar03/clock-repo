from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock")

icon = PhotoImage(file='logo.png')
root.iconphoto(True, icon)


def time():
    string = strftime("%I:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("DS-digital", 100), background="black", foreground="white")
label.pack(anchor='center')

time()

mainloop()
