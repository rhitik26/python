Products=[
    {
        "pid":"1",
        "name":"Asus1",
        "cost":"50000",
        "brand":"Asus",
        "rating":4,
        "discount":10,
        "category":"Laptop"
    },
       {
        "pid":"2",
        "name":"Hp1",
        "cost":"60000",
        "brand":"Hp",
        "rating":4.5,
        "discount":12,
        "category":"Laptop"
    },
       {
        "pid":"3",
        "name":"Lenovo1",
        "cost":"40000",
        "brand":"Lenovo",
        "rating":4.2,
        "discount":14,
        "category":"Laptop"
    },
       {
        "pid":"4",
        "name":"Asus2",
        "cost":"50000",
        "brand":"Asus",
        "rating":4.4,
        "discount":11,
        "category":"Laptop"
    },
       {
        "pid":"5",
        "name":"Hp2",
        "cost":"50000",
        "brand":"Hp",
        "rating":4.5,
        "discount":17,
        "category":"Laptop"
    },
       {
        "pid":"6",
        "name":"Lenovo2",
        "cost":"100000",
        "brand":"Lenovo",
        "rating":4.7,
        "discount":7,
        "category":"Laptop"
    }
]
ch=0
print('1:sort by cost low to high')
print('2:sort by cost high to low')
print('3:sort by rating low to high')
print('4:sort by rating high to low')
print('5:sort by discount low to high')
ch=int(input())
dict={1:['cost',False],2:['cost',True],3:['rating',False],4:['rating',True],5:['discount',True]}
Products.sort(key=lambda el:el[dict[ch][0]],reverse=dict[ch][1])
print(Products)