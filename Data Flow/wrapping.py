def outer(a):
    def inner(*ar,**k):
        print("This is inner")
        a(*ar,**k)
        print("Inner finished")
    return inner
@outer    
def hello(n):
    print("Hello "+n)
@outer  
def sayhi(n1,n2):
    print("Hi "+n1+" and "+n2)   
#hello=outer(hello)
hello("Sachin")
#sayhi=outer(sayhi)
sayhi(n1="Virat",n2="Dhoni")