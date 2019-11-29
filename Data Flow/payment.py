def wallet(balance):
    def deposit(amount):
        nonlocal balance
        balance=balance+amount
        print(str(amount)+" deposited new balance is: "+str(balance))
    def withdraw(amount):
        nonlocal balance
        if(balance<amount):
            print("Not possible")
        else:
            balance=balance-amount
            print(str(amount)+' withdrawn new balance is: '+str(balance))
    def transfer(amt):
        r1=wallet(10)
        print (r1[0](amt))
        print('amount transfered')
    return [deposit,withdraw,transfer]
balance=int(input('Enter initial balance'))
r=wallet(balance)
ch=int(input('1 to deposit and 2 to withdraw and 3 to transfer'))
if ch==1:
    ad=int(input('amount to deposit'))
    r[0](ad)
elif ch==2:
    aw=int(input('amount to withdraw'))
    r[1](aw)
else:
    amt=int(input('enter amount'))
    r[2](amt)
    r[1](amt)
      