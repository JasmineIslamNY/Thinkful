import sys
counter = 1

while True:
	try:
		if len(sys.argv) > 1:
			limit = int(sys.argv[1])
		else:
			limit = int(raw_input("Please enter a number to count fizzbuzz up to: "))
		break
	except ValueError:
		try:
			limit = int(raw_input("Please enter a number to count fizzbuzz up to: "))
			break
		except ValueError:
			print "Please try a whole number"
			
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




