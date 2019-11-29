#Sequence Operation
#indexing
data="Hello World"
print(data[0])#first
print(data[2])
print(data[-1])#last
print(data[-3])

#Slicing
print(data[0:5])#5th index excluded
print(data[6:])#nothing means last of file
print(data)

#stepping
print(data[0::2])#3rd parameter tells no. of character to be skipped
print(data[10:5:-1])