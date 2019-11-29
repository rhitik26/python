marks=int(input('Enter Marks'))
if marks>=0 and marks<=100:
    if marks>=0 and marks<=39:
        print("Fail")
    elif marks>=40 and marks<60:
        print("Third")
    elif marks>=60 and marks<80:
        print("Second")
    else:
        print("First")
