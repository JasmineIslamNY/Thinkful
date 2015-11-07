class Item(object):
	def __init__(self, value):
		self.value = value
		self.nextItem = None

	def setNextItem(self, item):
		self.nextItem = item


class Queue(object):
	def __init__(self):
		self.count = 0
		self.head = None
		self.end = None	

	def enqueue(self, value):
		item = Item(value)
		if (self.head == None):
			self.head = item
			self.end = item
		else:
			currItem = self.end
			currItem.setNextItem(item)
			self.end = item
		self.count += 1
	
	def dequeue(self):
		if (self.head == None):
			print("Empty List")
		else:
			itemToReturn = self.head
			self.head = itemToReturn.nextItem
			itemToReturn.setNextItem(None)
			self.count -= 1
			return itemToReturn.value

	def peek(self):		
		if (self.head == None):
			return []
		else:
			currItem = self.head
			list = []
			index = 0
			for i in range(0,self.count):
				list.append(currItem.value)
				currItem = currItem.nextItem
			return list

if __name__ == "__main__":
	queue = Queue()
	print queue.peek()
	print("Adding to the queue")
	queue.enqueue(7)
	queue.enqueue(6)
	queue.enqueue(5)
	queue.enqueue(4)
	print queue.peek()
	print("Removing from queue")
	value = queue.dequeue()
    	print("dequeued {} from queue".format(value))
	print queue.peek()