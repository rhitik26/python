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
s1=student("rhitik","SRM")
s1.study()
s1.sayhi()