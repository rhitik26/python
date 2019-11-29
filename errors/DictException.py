dict={"sachin":"qwerty","virat":"yyyy","dhoni":"98uj"}
try:
    a=input('enter username')
    b=input('enter password')
    if a not in dict:
        raise Exception("username not found")
    
    if b!= dict[a]:
        raise Exception("Password not found")
    else:
        print ("correct id and password")
except Exception as e:
    print(e)