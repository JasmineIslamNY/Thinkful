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
	currIndex = 1
	temp = 0
	
	if (len(array) == 1) | (len(array) == 0):
		return array

	while currIndex < len(array):
		follower = currIndex
		while follower > 0:
			if array[follower - 1] > array[follower]:
				temp = array[follower - 1]
				array[follower - 1] = array[follower]
				array[follower] = temp
			follower -= 1
		currIndex += 1		
	return array



if __name__ == "__main__":
	#create array (list) of specified size
	array = create_randomint_array(5, 100)

	print("Array before the sort")
	print_array(array)

	#sort the array
	array_sort(array)

	print("Array after the sort")
	print_array(array)

