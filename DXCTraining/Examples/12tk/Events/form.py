from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
s1=StringVar()
entry_1 = Entry(root,textvariable=s1)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
s2=StringVar()
entry_2 = Entry(root,textvariable=s2)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

s4=StringVar()
entry_4 = Entry(root,textvariable=s4)
entry_4.place(x=240,y=280)
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
root.mainloop()
print("registration form  seccussfully created...")
print(s1.get())
print(s2.get())
print(s4.get())