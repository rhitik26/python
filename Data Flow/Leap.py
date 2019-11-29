year=int(input('enter year'))
if year%100==0:
    if year%400==0:
        print('Leap Year 2')
    else:
        print("Not Leap Year")
else:
    if year%4==0:
        print("Leap Year")
    else:
        print("Not Leap Year")