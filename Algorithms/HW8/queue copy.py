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

	def addFront(self, value):
		item = Item(value)
		item.setNextItem(self.head)
		self.head = item
		self.count += 1

	def addEnd(self, value):
		item = Item(value)
		if (self.head == None):
			self.head = item
		else:
			currItem = self.head
			while (currItem.nextItem != None):
				currItem = currItem.nextItem
			currItem.setNextItem(item)
		self.count += 1
	
	def removeFront(self):
		if (self.head == None):
			print("Empty List")
		else:
			itemToReturn = self.head
			self.head = itemToReturn.nextItem
			itemToReturn.setNextItem(None)
			self.count -= 1
			return itemToReturn
			
	def removeEnd(self):
		if (self.head == None):
			print("Empty List")
		else:
			currItem = self.head
			beforeCurrItem = None
			while(currItem.nextItem != None):
				beforeCurrItem = currItem
				currItem = currItem.nextItem
			itemToReturn = currItem
			beforeCurrItem.nextItem = None
			self.count -= 1
			return itemToReturn

	def removeAtIndex(self, index):
		if(index == 0):
			self.removeFront()
		elif (index >= (self.count -1)):
			self.removeEnd()
		else:
			currItem = self.head
			beforeCurrItem = None
			for i in range(0,index):
				beforeCurrItem = currItem
				currItem = currItem.nextItem
			beforeCurrItem.setNextItem(currItem.nextItem)
			currItem.setNextItem(None)
			self.count -= 1
			return currItem

	def addAtIndex(self, index, value):
		if(index == 0):
			self.addFront(self, value)
		elif (index >= (self.count)):
			if index > self.count:
				print("Requested position greater than list size, adding to the end")
			self.addEnd(self, value)
		else:
			item = Item(value)
			currItem = self.head
			for i in range(0,index-1):
				currItem = currItem.nextItem
			afterCurrItem = currItem.nextItem
			currItem.setNextItem(item)
			item.setNextItem(afterCurrItem)
			self.count += 1

	def getIndex(self, number):		
		if (self.head == None):
			print("Empty List")
		else:
			currItem = self.head
			index = 0
			for i in range(0,self.count):
				if currItem.value == number:
					return index
				else:
					currItem = currItem.nextItem
					index += 1
			print("Not found in list")
	

	def display(self):		
		if (self.head == None):
			print("Empty List")
		else:
			currItem = self.head
			index = 0
			for i in range(0,self.count):
				print("The value of index {} is {}.".format(index, currItem.value))
				currItem = currItem.nextItem
				index += 1

if __name__ == "__main__":
	ll = LinkedList()
	ll.display()
	print("Adding to the front")
	ll.addFront(7)
	ll.addFront(6)
	ll.addFront(5)
	ll.addFront(4)
	ll.display()
	print("Adding to the front the value 13")
	ll.addFront(13)
	ll.display()
	print("Adding to the end the value 56")
	ll.addEnd(56)
	ll.display()
	print("Calling get Index for value 7")
	print(ll.getIndex(7))
	print("Calling get Index for value not in the list")
	print(ll.getIndex(20))
	print("Adding at Index 3, value 99")
	ll.addAtIndex(3, 99)
	ll.display()
	print("Removing from Index 2")	
	ll.removeAtIndex(2)
	ll.display()
	print("Removing from the end")		
	ll.removeEnd()
	ll.display()
	print("Removing from the front")	
	ll.removeFront()
	ll.display()

