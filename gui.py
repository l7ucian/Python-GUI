from tkinter import *

def callback():
    print(e1_value.get())
    t1.insert(END,e1_value.get())

window = Tk()

b1 = Button(window, text = 'Execute',command=callback)
b1.grid(row=0, column=1)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=0,column=2)

window.mainloop()