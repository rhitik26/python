
def outer():
    c=0#global keyword is used to make changes in global variable
    def inner():
        nonlocal c
        c+=1
        print(c)
    return inner
h=outer()
h()
h()
#Above Mentioned Concept is known Closures