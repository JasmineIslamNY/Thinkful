def side_effect_test(value):
     # Do something to modify the value     
	value[2] = "Bob"     
	print "Inside the function, the value becomes {}".format(value)  

if __name__ == "__main__":     
	# Create the value     
	value = ('Charles', 'Will', 'Robert', 'Claire')

	print "Outside the function, the value starts as {}".format(value)      

	side_effect_test(value)      
	
	print "Outside the function, the value is now {}".format(value) 
