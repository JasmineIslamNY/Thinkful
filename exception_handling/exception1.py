while True:
	try:
		n = raw_input("Please enter an integer: ")
		n = int(n)
		break
	except ValueError:
		print("No Valid Integer! Please try again!")

print "Great, you successfully entered an integer!"
