n=int(input('enter number'))
i=2
c=1
#s=1
while i<=n/2:
    if n%i==0:
        #print(i)
        c=c+1
        break
    i=i+1
if c>1:
    print("Not Prime")
else:
    print("prime")