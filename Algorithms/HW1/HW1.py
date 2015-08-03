from array import *
import argparse

def make_parser():
    """ Construct the command line parser """
    description = "Create a specified sized list and fill with random numbers from 0 to specified limit"
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument("ListSize", help="The size of the list you want to create, default is 5")
    parser.add_argument("UpperLimit", help="Enter the upper limit of the random numbers, default is 100")
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
    
	print("Array before the sort")
	Array.print_array(myArray)

	#sort the array
	Array.array_sort(myArray)

	print("Array after the sort")
	Array.print_array(myArray)

if __name__ == "__main__":
    main()






