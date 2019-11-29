import re
# p='\st[a-z]*|^t[a-z]*'
# t='Tom, does this match the pattern'
# m=re.search(p,t)
# m1=re.findall(p,t,re.I)
# print(m1)
# print(re.search(p,t))
# for i in m1:
#      print('found a match')
#      print(i.start(),i.end(),t[i.start():i.end()])
# else:
#     print('not found')
a=input()
if re.search('^[0-9]{10}$',a):
    print('valid')
else:
    print("invalid")