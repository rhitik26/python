#Every variable declared outside a function is a global variable
data="Hi" #global variable
def d():
  #  print(data)
    d1="Hello" #Local Variable
t=d()#here t will have value value returned by d()
#print(type(t))

def c(a):
   # print(type(a))
    a()
c(d)

#def outer():
   # print("this is outer")
 #   def inner():
       # print("this is inner")
  #  inner()
#outer()


