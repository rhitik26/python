import json
fo=open('demo.txt','r')
li=json.load(fo)
for d in li:
	print(d)
print(li[1]['address']['city'])
fo.close()

#to read a json string we use json.loads
#to write json data to another file we use json.dump(json_data,file with open mode as write)
#to write json data to server we use json.dumps(json_data)