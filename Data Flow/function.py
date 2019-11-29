#Variable length positional arguments
def add(*args):
   # print(type(args))
    #print(type(args))
    s=0
    for i in args:
        s=s+i
    return(s)
print(add(1,2))
print(add(1,2,3))


#variable length keyworded arguments
def Sayhi(**a):
    print(type(a))
    print(a.values())
Sayhi(name1='Sachin',name2='dhoni')

#Generic Function 
def sayhello(*a,**b):
    print(a,b)
sayhello(1,2)
sayhello(n1='x',n2='y')
sayhello(1,n1='r')

def sayhi(n1,n2,n3):
    print(n1+' '+n2+' '+n3)
li={
"n1":"Sachin",
"n2":"Kohli",
"n3":"Dhoni"}
sayhi(**li)

