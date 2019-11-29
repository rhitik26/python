#SETS
s1={1,None,'Hello',True,2.3}
print(type(s1))
print(s1)

#UNION
s1={1,2,3,4}
s2={5,6,7}
s3={2,3}
print(s1|s2)

#INTERSECTION
print(s1&s2)

#DIFFERENCE
print(s1-s2)
print(s2-s1)

#ISSUBSET
print(s3<s1)
#List to Set Conversion
l1=[1,1,4,4]
print(set(l1))

#Dict to Set Conversion
d1={'fname':'Rhtik','lname':'khanna','fname':'Rishabh'}
print(set(d1.values()))

#Tupple to Set Conversion
t1=1,1,1,1
print(set(t1))

