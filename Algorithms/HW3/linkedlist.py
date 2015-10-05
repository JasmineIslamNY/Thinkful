class Node(object):
	def __init__(self, payload):
		self.payload = payload
		self.nextNode = None

	def setNextNode(self, node):
		self.nextNode = node


class LinkedList(object):
	def __init__(self):
		self.count = 0
		self.head = None	

	def addFront(self, value):
		node = Node(value)
		node.setNextNode(self.head)
		self.head = node
		self.count += 1

	def addEnd(self, value):
		node = Node(value)
		if (self.head == None):
			self.head = node
		else:
			currNode = self.head
			while (currNode.nextNode != None):
				currNode = currNode.nextNode
			currNode.setNextNode(node)
		self.count += 1
	
	def removeFront(self):
		if (self.head == None):
			print("Empty List")
		else:
			nodeToReturn = self.head
			self.head = nodeToReturn.nextNode
			nodeToReturn.setNextNode(None)
			self.count -= 1
			return nodeToReturn
			
	def removeEnd(self):
		if (self.head == None):
			print("Empty List")
		else:
			currNode = self.head
			beforeCurrNode = None
			while(currNode.nextNode != None):
				beforeCurrNode = currNode
				currNode = currNode.nextNode
			nodeToReturn = currNode
			beforeCurrNode.nextNode = None
			self.count -= 1
			return nodeToReturn

	def removeAtIndex(self, index):
		if(index == 0):
			self.removeFront()
		elif (index >= (self.count -1)):
			self.removeEnd()
		else:
			currNode = self.head
			beforeCurrNode = None
			for i in range(0,index):
				beforeCurrNode = currNode
				currNode = currNode.nextNode
			beforeCurrNode.setNextNode(currNode.nextNode)
			currNode.setNextNode(None)
			self.count -= 1
			return currNode

	def addAtIndex(self, index, value):
		if(index == 0):
			self.addFront(self, value)
		elif (index >= (self.count)):
			if index > self.count:
				print("Requested position greater than list size, adding to the end")
			self.addEnd(self, value)
		else:
			node = Node(value)
			currNode = self.head
			for i in range(0,index-1):
				currNode = currNode.nextNode
			afterCurrNode = currNode.nextNode
			currNode.setNextNode(node)
			node.setNextNode(afterCurrNode)
			self.count += 1

	def getIndex(self, value):		
		if (self.head == None):
			print("Empty List")
		else:
			currNode = self.head
			index = 0
			for i in range(0,self.count):
				if currNode.payload == value:
					return index
				else:
					currNode = currNode.nextNode
					index += 1
			print("Not found in list")
	

	def display(self):		
		if (self.head == None):
			print("Empty List")
		else:
			currNode = self.head
			index = 0
			for i in range(0,self.count):
				print("The value of index {} is {}.".format(index, currNode.payload))
				currNode = currNode.nextNode
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

