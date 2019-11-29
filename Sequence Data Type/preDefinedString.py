str="hello world!"
#print(len(str))
#print(str.index('o'))
#print(str.index('o',5))
#print(str.index('o',5,8))
#print(str.count('l'))
#print(str.upper())
#print(str.lower())
#print(str.startswith('h'))
#print(str.endswith('!'))
#print(str.split(" "))
#print(str.find('o'))
#print(str.find('o',5))
#print(str.find('o',5,7))
#print(str.replace('world',"rhitik"))

#Template String Formatting
data='I am a {0} from {1}'
sub1="String"
l="Python"
print(data.format(sub1,l))

obj=[{"fname":"rhitik","lname":"khanna","city":"Delhi"},{"fname":"yash","lname":"chawla","city":"kanpur"}]
t="hello {fname} {lname},Welcome to {city}"
for i in obj:
    print(t.format(**i))