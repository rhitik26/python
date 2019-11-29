rows=int(input('enter no. of rows'))
i=rows
j=0
while i>=0 and j<=rows:
    print(" "*j+"*"*i)
    i=i-1
    j=j+1
        
print("------------------------------")

str='python'
i=0
j=rows
while i<=rows:
    print(str[0,i])
    i=i+1
    j=j-1
    
