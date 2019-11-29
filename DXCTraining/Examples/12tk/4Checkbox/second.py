from tkinter import *
def sel():
    selection=var.get()
    label.config(text = selection) 
master = Tk()

var = StringVar()
c = Checkbutton(
        master, text="Color image", 
		variable=var,
        onvalue="RGB", offvalue="BW",command=sel
        )
label=Label(master)
c.pack()
label.pack()
mainloop()