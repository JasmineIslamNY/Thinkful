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
	def array_sort_bubble(array):
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

	@staticmethod
	def array_sort_merge(array, low, high):
		if (high - low <= 1):
			return array

		mid = ((high - low)/2) + low
		"""
		print ("Low is {}".format(low))
		print ("Mid is {}".format(mid))
		print ("High is {}".format(high))
		print ("Array is:")
		Array.print_array(array)
		print ("Array length is {}".format(len(array)))
		"""

		Array.array_sort_merge(array, low, mid)
		Array.array_sort_merge(array, mid+1, high)
		Array.array_merge(array, low, mid, high)

		return array

	@staticmethod
	def array_merge(array, low, mid, high):

		temp_array = []
		mid2 = mid + 1
		l = low
		m2 = mid2
		
		for i in range(low, high+1):
			if l == mid2:
				temp_array.append(array[m2])
				m2 += 1
			elif m2 > high:
				temp_array.append(array[l])
				l += 1		
			elif array[l] <= array[m2]:
				temp_array.append(array[l])
				l += 1
			else:
				temp_array.append(array[m2])
				m2 += 1
			i += 1	

		for i in range(0, len(temp_array)):
			array[low] = temp_array[i]
			low +=1

		return array

	
