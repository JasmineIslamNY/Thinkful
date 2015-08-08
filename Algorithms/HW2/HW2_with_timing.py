from array import *
import time
import argparse

def make_parser():
    """ Construct the command line parser """
    description = "Create a specified sized list and fill with random numbers from 0 to specified limit"
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument("-ListSize", nargs='?', default = 5, help="The size of the list you want to create, default is 5")
    parser.add_argument("-UpperLimit", nargs='?', default = 100, help="Enter the upper limit of the random numbers, default is 100")
    return parser

def main():
	parser = make_parser()
	args = parser.parse_args()


	try:
		list_size = int(args.ListSize)
		upper_limit = int(args.UpperLimit)

		#create array (list) of specified size
		myArray = Array.create_randomint_array(list_size, upper_limit)

	except :
		print("One of the entries was not an integer, using defaults")
		myArray = Array.create_randomint_array(5, 100)
    
	myArray2 = []
	for i in range(0, len(myArray)):
		myArray2.append(myArray[i])
		i +=1
		
	print("Arrays before the sort")
	print("MyArray:")
	Array.print_array(myArray)
	print("MyArray2:")
	Array.print_array(myArray2)

	#Bubble Sort
	start_time = time.time()
	Array.array_sort_bubble(myArray)
	elapsed_time = time.time() - start_time

	print("Array after the sort")
	Array.print_array(myArray)


	
	#Merge Sort
	start_time2 = time.time()
	Array.array_sort_merge(myArray2)
	elapsed_time2 = time.time() - start_time2

	print("Array after the sort")
	Array.print_array(myArray2)



	print("Bubble sort took {} seconds".format(elapsed_time))
	print("Merge sort took {} seconds".format(elapsed_time2))

	

if __name__ == "__main__":
    main()






