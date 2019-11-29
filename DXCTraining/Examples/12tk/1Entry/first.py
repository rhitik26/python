# !/usr/bin/python3
from tkinter import *

tkit = Tk()
L1 = Button(tkit, text = "User Name:")
L1.pack( side = LEFT)
E1 = Entry(tkit, bd = 1)
E1.pack(side = RIGHT)

tkit.mainloop()