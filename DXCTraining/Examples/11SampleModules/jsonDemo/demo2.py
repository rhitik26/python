import json
data=[
	{
		"id":1,
		"fname":"Sachin" ,
		"lname":"Tendulkar",
		"address":{
					"houseno":17,
					"streetno":19,
					"area":"worli",
					"city":"Mumbai",
					"pin":1223445
					}
	},
	{
		"id":1,
		"fname":"Sachin" , 
		"lname":"Tendulkar",
		"address":{
					"houseno":17,
					"streetno":19,
					"area":"worli",
					"city":"Mumbai",
					"pin":1223445
					}
	},
	{
		"id":1,
		"fname":"Sachin" ,
		"lname":"Tendulkar",
		"address":{
					"houseno":17,
					"streetno":19,
					"area":"worli",
					"city":"Mumbai",
					"pin":1223445
					}
	}
]

j=json.dumps(data)
json.dump(data,open('sample.txt','w'))
print(j)