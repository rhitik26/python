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
class student(person):
    def __init__(o,f,u):
        person.__init__(o,f)
        o.university=u
    def study(o):
        print(o.fname+" Studying at "+o.university)
class intern(student,emp):
    def __init__(o,f,d,u,l):
        student.__init__(o,f,u)
        emp.__init__(o,f,d)
        o.location=l
    def internship(o):
        print(o.fname+" "+o.dept+" "+o.university+" "+o.location)
    def __int__(o):
        return len(o.fname)+len(o.university)
i1=intern("Rhitik","IT","SRM","Delhi")
i1.internship()
print(int(i1))