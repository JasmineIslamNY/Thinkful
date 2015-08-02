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
	follower = 1
	counter = 1 #what is this for?
	temp = 0
	
	while (follower != len(array)) & (len(array) > 0):
		for i in range(follower):
			if array[i] > array[follower]:
				temp = array[i]
				array[i] = array[follower]
				array[follower] = temp
		follower += 1
			
	return array



if __name__ == "__main__":
	#create array (list) of specified size
	array = create_randomint_array(5, 100)

	#print the array
	print("Array before the sort")
	print_array(array)

	#sort the array
	array_sorted = array_sort(array)

	#print the array after sort
	print("Array after the sort - array")
	print_array(array)
	print("Array after the sort - array_sorted")
	print_array(array_sorted)


