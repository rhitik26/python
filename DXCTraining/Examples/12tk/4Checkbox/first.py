# !/usr/bin/python3
from tkinter import *

import tkinter
def sel():
    d=["Music","Videos"]
    i=0
    res=""
    for l in li:
        if l.get():
            res+=d[i]+" "
        i+=1
        # sele=l.get()
        label.config(text =res)
top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
li=[CheckVar1,CheckVar2]
C1 = Checkbutton(top, text = "Music", 
				variable = CheckVar1, 
                 onvalue = 1, 
				 offvalue = 0, 
				 height=5, 
                 width = 20,command=sel )
C2 = Checkbutton(top, 
				text = "Video", 
				variable = CheckVar2, 
                 onvalue = 1, 
				 offvalue = 0, 
				 height=5, width = 20,command=sel)
label=Label(top)                 
C1.pack()
C2.pack()
label.pack()
top.mainloop()