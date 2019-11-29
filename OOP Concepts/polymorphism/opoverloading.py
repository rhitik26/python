class Box:
    def __init__(o,l):
        o.l=l
    def __str__(s):
        return str(s.l)
    def __add__(s,ot):
        newitems=s.l+ot.l
        b=Box(newitems)
        return b
    def __lt__(s,o):
        return len(s.l)<len(o.l)
b1=Box(["i1","i2"])
b2=Box(["i3","i4","i5"])
b3=b1+b2
print(b1)
print(b2)
print(b3)
print(b1>b2)