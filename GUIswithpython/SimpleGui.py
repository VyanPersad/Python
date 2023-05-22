#We use this so we can get all of the tkinter library
from tkinter import *

window = Tk()


def cm_to_ins():
    #print(e1_val.get())
    ins = float(e1_val.get()) / 2.55
    t1.insert(END, ins)


#For a button to work then command should pass a function without the brackets
b1 = Button(window, text="Execute", command=cm_to_ins)
b1.grid(row=0, column=0)
#This defines the input for the GUI
e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)
#This defines the output for the GUI
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

#This must be the
#  last thing in your code.
window.mainloop()