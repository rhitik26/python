n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
else:
	print('Loop exhausted!!!')

print("Sum of 1 until %d: %d" % (n,sum))