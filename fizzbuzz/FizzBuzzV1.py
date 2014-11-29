# how high to count up to
limit = 100
counter = 1

print "Fizz buzz counting up to {}".format(limit)

while counter <= limit:
	if (counter % 3 == 0) and (counter % 5 == 0):
		print "fizzbuzz"
	elif (counter % 3 == 0):
		print "fizz"
	elif (counter % 5 == 0):
		print "buzz"
	else:
		print counter 
	counter += 1


print "Finished counting!"

