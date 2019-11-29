l=['a','b','c','d','e','f','e','a']
print(len(l))
#print(sum(l))
print(max(l))
print(min(l))
l.append('g')
print(l)
l2=['i','j','k']
l.extend(l2)
print(l)
l.insert(2,'z')
print(l)
print(l.pop(2))
print(l)
l.remove('a')
print(l)
l.reverse()
print(l)
l.sort(reverse=True)
print(l)
print(l.count('e'))

obj=[{"fname":"rhitik","lname":"khanna","city":"Delhi"},{"fname":"yash","lname":"chawla","city":"kanpur"}]
mysort=lambda el:el['lname']
#def mysort(el):
    #print("mysort called "+el["lname"])
   # return el["lname"]
obj.sort(key=mysort)
print(obj)

#Filtering
myfilter=lambda el:el['fname'].startswith('y')
#def myfilter(el):
    #return el["city"]=="Delhi"
 #   return el["fname"].startswith('y')
newObj=filter(myfilter,obj)
for i in newObj:
    print('{fname} {lname} '.format(**i))
    
    
#Mapping
ob1=[22,32,44,56]
mymap=lambda el:32+el*9/5
#def mymap(el):
 #   return 32+el*9/5
nw=map(mymap,ob1)
for i in nw:
    print(i)




#Anonymous/lamba/inline Function
#Rule1:Function should have only one line
#Rule 2:that one line should be return statement
s=lambda n1,n2: "Hi "+n1+" "+n2
#s("Rhitik","Khanna")
print(s("Rhitik","Khanna"))


add=lambda n3,n4: n3+n4
print(add(3,4))
print(add(30,40))
print(add(300,400))

n=int(input('enter any number'))
r=list(range(1,n+1))
l=filter(lambda i:n%i == 0,r)
print(list(l))