def allString(a):
    def inner(*ar,**k):
        for i in ar:
            if type(i)!=str:
                print("Invalid Argument type")
                break
        else:
            for i in k.values():
                if type(i)!=str:
                    print("Invalid keyworded argument type")
                    break
            else:
                a(*ar,**k)
    return inner
@allString
def hello(n):
    print("Hello "+n)
@allString  
def sayhi(n1,n2):
    print("Hi "+n1+" and "+n2)
hello("Sachin")
sayhi(n1="Virat",n2="Dhoni")
hello(1)
sayhi(n1=2,n2=3)