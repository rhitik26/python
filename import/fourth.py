import os.path
import re
# filename='C:/Users/rkhanna36/Documents/Python/import/first.py'
# print(os.path.splitext(filename))
# print(os.path.dirname(filename))
# print(os.path.basename(filename))
# print(os.path.exists(filename))
# print(os.path.isabs(filename))
# print(os.path.isdir(filename))
# print(os.path.isfile(filename))
# print(os.path.islink(filename))
# os.environ['user']="root"
# vp='usr/$user/appdata'
# ap=os.path.expandvars(vp)
# print(ap)
# os.chdir('./assignment')
p='C:/Users/rkhanna36/Documents/Python/import/assignment'
f=os.listdir(p)
# print(os.getcwd())
print(f)
for d in f:
    if(os.path.splitext(d)[1]=='.txt'):
        data=open(p+'/'+d,'r')
        # print(data.read())
        m1=re.findall('[a-zA-Z0-9]+@[a-zA-z]+\.[a-zA-Z]+',data.read())
        print(m1)

