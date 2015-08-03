from random import randint

class Array(object):

	def __init__(self, name):
		self.name = name

	@staticmethod
	def create_randomint_array(array_size, number_size):
		"""create array with specified size and fill with a random integer from 0 to number_size
		"""
		list = []
		for i in range(array_size):
			list.append(randint(0,number_size))
		return list

	@staticmethod
	def print_array(array):
		for i in range(len(array)):
			print array[i]

	@staticmethod
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
				else:
					break
				follower -= 1
			currIndex += 1		
		return array

