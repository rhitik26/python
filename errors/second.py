try:
    names=["Sachin","Virat","Dhoni"]
    name=input("Enter name: ")
    if name not in names:
        raise Exception("Name not found")
    print("Welcome "+name)
except Exception as ex:
    print("hi ",ex)
print("Some other task")