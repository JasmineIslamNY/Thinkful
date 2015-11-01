class Disk(object):
	def __init__(self, size):
		self.size = size
		self.nextDisk = None

	def setNextDisk(self, disk):
		self.nextDisk = disk


class Stack(object):
	""" Each Stack has a count and the methods push (include a numeric size for the disk), pop (which returns the size of the disk), and peek (which returns a list with the sizes of the disks) """

	def __init__(self):
		self.count = 0
		self.head = None	

	def push(self, size):
		disk = Disk(size)
		if self.count == 0:
			self.head = disk
			self.count += 1
			return 1
		elif disk.size < self.head.size:
			disk.setNextDisk(self.head)
			self.head = disk
			self.count += 1
			return 1
		else:
			return -1
	
	def pop(self):
		if (self.head == None):
			return -1
		else:
			diskToReturn = self.head
			self.head = diskToReturn.nextDisk
			diskToReturn.setNextDisk(None)
			self.count -= 1
			return diskToReturn.size	

	def peek(self):		
		if (self.head == None):
			return []
		else:
			currDisk = self.head
			list = []
			for i in range(0,self.count):
				list.append(currDisk.size)
				currDisk = currDisk.nextDisk
			return list

if __name__ == "__main__":
	stack = Stack()
	print stack.peek()
	print("Adding to the stack")
	stack.push(7)
	stack.push(6)
	stack.push(5)
	stack.push(4)
	print stack.peek()
	print("Removing from Stack")
	value = stack.pop()
    	print("Popped {} from stack".format(value))
	print stack.peek()
	print("Adding invalid value")
	value = stack.push(8)
    	print value
    	print stack.peek()

