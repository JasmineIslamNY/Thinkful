from random import randint

def create_randomint_array(array_size, number_size):
	"""create array with specified size and fill with a random integer from 0 to number_size
	"""
	list = []
	for i in range(array_size):
		list.append(randint(0,number_size))
	return list

def print_array(array):
	for i in range(len(array)):
		print array[i]

def array_sort(array):
	



if __name__ == "__main__":
	#create array (list) of specified size
	array = create_randomint_array(5, 100)

	#print the array
	print_array(array)

	#sort the array
	array_sorted = array_sort(array)

	#print the array after sort
	print_array(array)
	print_array(array_sorted)


