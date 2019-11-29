class products:
    def __init__(o,id,name,rating,cost,discount,cat):
        o.id=id
        o.name=name
        o.rating=rating
        o.cost=cost
        o.discount=discount
        o.cat=cat
    def show(o):
        print(o.id+" "+o.name+" "+o.rating+" "+o.cost+" "+o.discount+" "+o.cat)
    def sortp(li,ch):
        dict={1:['cost',False],2:['cost',True],3:['rating',False],4:['rating',True],5:['discount',True]}
        li.sort(key=lambda el:getattr(el,dict[ch][0]),reverse=dict[ch][1])
       
obj1=products("1","Lenovo","4","50000","15%","electronics")
obj2=products("2","LG","5","10000","25%","Home Appliance")
obj3=products("3","Sony","2","60000","75%","Television")
l=[obj1,obj2,obj3]

print('1:sort by cost low to high')
print('2:sort by cost high to low')
print('3:sort by rating low to high')
print('4:sort by rating high to low')
print('5:sort by discount low to high')
ch=int(input())
products.sortp(l,ch)
for o in l:
    products.show(o)