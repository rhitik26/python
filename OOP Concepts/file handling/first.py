# fo=open('demo.txt','r')
# for l in fo:
    # print(l)
# #print(data)
# fo.close()

# fo=open('demo2.txt','wb')
# fo.write("HI Everyone \n".encode())
# fo.write("BYE \n".encode())
# fo.close()
# fo=open('demo2.txt','rb')
# for l in fo:
    # print(l.decode(),end="")
# fo.close()

fo=open('a1.png','rb')
data=fo.read()
fo.close()

fo=open('d3.png','wb')
fo.write(data)
fo.close()