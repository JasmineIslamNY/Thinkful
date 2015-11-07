class Item(object):
	def __init__(self, value):
		self.value = value
		self.nextItem = None

	def setNextItem(self, item):
		self.nextItem = item


class Stack(object):
	""" Each Stack has a count and the methods push (include a value for the item), pop (which returns the value of the item), and peek (which returns a list with the values of the items) """

	def __init__(self):
		self.count = 0
		self.head = None	

	def push(self, value):
		item = Item(value)
		if self.count == 0:
			self.head = item
			self.count += 1
		else:
			item.setNextItem(self.head)
			self.head = item
			self.count += 1
	
	def pop(self):
		if (self.head == None):
			return None
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
			for i in range(0,self.count):
				list.append(currItem.value)
				currItem = currItem.nextItem
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


