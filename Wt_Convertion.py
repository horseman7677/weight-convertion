import tkinter 
from tkinter import *
window = Tk()

def func():
    gram = float(e2_value.get()) * 1000
    pound = float(e2_value.get()) * 2.20462
    ounce = float(e2_value.get()) * 35.274

    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)

def clear():
    e2.delete(0, END)
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)

window.minsize(500 , 350)
window.maxsize(500 , 350)

#create a local widget
e1 = Label(window, text="Enter The Wieght(Kg)")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value, bg="light yellow")
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pounds")
e5 = Label(window, text="Ounce")

#create text widget
t1 = Text(window, height=1 , width=10, bg="light yellow")
t2 = Text(window, height=1 , width=10, bg="light yellow")
t3 = Text(window, height=1 , width=10, bg="light yellow")

#create a local button
b1 = Button(window, text="Convert", command=func)
b2 = Button(window, text="Clear", command=clear)

#Allocating postion
e1.grid(row=0 , column=0)
e2.grid(row=0 , column=1)
b1.grid(row=0 , column=2)
b2.grid(row=0 , column=3)
e3.grid(row=1 , column=0)
e4.grid(row=1 , column=1)
e5.grid(row=1 , column=2)
t1.grid(row=2 , column=0)
t2.grid(row=2 , column=1)
t3.grid(row=2 , column=2)

window.mainloop()