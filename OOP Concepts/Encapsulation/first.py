class person:
    '''
    this is demo
    '''
    team="India"     #Class Level Encapsulation
    def sayhi(p):
        print("Hi "+p.fname+" "+p.lname)
    def __init__(o,f,l):
        o.fname=f
        o.lname=l
obj=person("Sachin","Tendulkar")
#print(type(obj))                #this is print main.person
#obj.fname="Sachin"               #Object level encapsulation
#obj.lname="Tendulkar"
print(obj.fname,obj.lname,obj.team)
obj2=person("Virat","Kohli")
#obj2.setVal()
#obj2.team="India"
print(obj2.fname,obj2.lname,obj2.team)
obj2.team="RCB"
print(obj.team,obj2.team,obj2.__class__.team)
obj.sayhi()                      #this is same as person.sayhi(obj)
obj2.sayhi()
setattr(obj,"PAN","uuujjj122")
print(obj.PAN)
print(getattr(obj,"PAN"))
print(hasattr(obj,"PAN"))
delattr(obj,"PAN")
print(hasattr(obj,"PAN"))
print(person.__name__)
print(person.__module__)
print(person.__doc__)
print(person.__dict__)