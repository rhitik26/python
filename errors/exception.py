try:
    a=int(input('enter number 1 '))
    b=int(input('enter number 2 '))
    d=a/b
    print('data: ',d)
except ZeroDivisionError as e:
    print(e)
except ValueError as ex:
    print(ex)
except Exception as ex:
    print("Generic Exception")
    
print("Some other task")