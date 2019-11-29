class person:
    nationality="India"
    def sayhi(o):
        print("hi "+o.fname)
    def __init__(o,f):
        o.fname=f
class emp(person):
    org="DXC"
    def __init__(ob,f,d):
        person.__init__(ob,f)
        ob.dept=d
    def work(o):
        print(o.fname+" is working in "+o.dept)
class manager(emp):
    def __init__(o,f,d,r):
        emp.__init__(o,f,d)
        o.reportees=r
    def manage(o):
        print(o.fname)
e1=manager("rhitik","IT",[])
#e1.fname="rhitik"
e1.work()
e1.sayhi()
e1.manage()
print(e1.org)
print(e1.nationality)
print(emp.__bases__)
print(person.__bases__)