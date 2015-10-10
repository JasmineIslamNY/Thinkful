class Node(object):
	def __init__(self, payload):
		self.payload = payload
		self.leftNode = None
		self.rightNode = None


class BinarySearchTree(object):
	def __init__(self):
		self.count = 0
		self.root = None	

	def addToTree(self, value):
		node = Node(value)
		if self.root == None:
			self.root = node
			self.count += 1
		else:
			self.addNodeToTree(self.root, node)
		
	def addNodeToTree(self, parent, child):
		if child.payload <= parent.payload:
			if parent.leftNode == None:
				parent.leftNode = child
				self.count += 1
			else:
				self.addNodeToTree(parent.leftNode, child)
		else:
			if parent.rightNode == None:
				parent.rightNode = child
				self.count += 1
			else:
				self.addNodeToTree(parent.rightNode, child)

	def findInTree(self, value):
		if self.count == 0:
			return -1
		else:
			if self.root.payload == value:
				return 1
			elif value < self.root.payload:
				self.findInChildTree(self.root.leftNode, value)
			else:
				self.findInChildTree(self.root.rightNode, value)

	def findInChildTree(self, node, value):
		if node == None:
			return -1
		elif node.payload == value:
			return 1
		elif value < node.payload:
			self.findInChildTree(node.leftNode, value)
		else:
			self.findInChildTree(node.rightNode, value)
	"""			
	def deleteFromTree(self, value):
		if self.count == 0:
			return "Empty Tree"
		else:
			if self.root.payload == value:
				return 1
			elif value < selfroot.payload:
				self.findInChildTree(self.root.leftNode, value)
			else:
				self.findInChildTree(self.root.rightNode, value)				

	"""
	def display(self):					
		if (self.count == 0):
			print("Empty Tree")
		else:
			print(self.root.payload)
			self.displayChildTree(self.root.leftNode)
			self.displayChildTree(self.root.rightNode)
			
	def displayChildTree(self, node):					
		if node == None:
			return -1
		else:
			print(node.payload)
			self.displayChildTree(node.leftNode)
			self.displayChildTree(node.rightNode)


	def findMax(self):
		if self.count == 0:
			return "Empty Tree"
		else:
			return self.findMaxInChild(self.root)

	
	def findMaxInChild(self, node):
		if node.rightNode == None:
			return node
		else:
			return self.findMaxInChild(node.rightNode)

	def findMin(self):
		if self.count == 0:
			return "Empty Tree"
		else:
			return self.findMinInChild(self.root)

	
	def findMinInChild(self, node):
		if node.leftNode == None:
			return node
		else:
			return self.findMinInChild(node.leftNode)
		

if __name__ == "__main__":
	t = BinarySearchTree()
	t.display()
	print("Adding")
	t.addToTree(7)
	t.addToTree(1)
	t.addToTree(6)
	t.addToTree(5)
	t.addToTree(34)
	t.addToTree(4)
	t.display()
	print("Finding Value 7")

	if t.findInTree(7) == 1:
		print ("Found 7")
	else:
		print("Did not find 7")

	print("Finding Value 20")
	if t.findInTree(20) == 1:
		print ("Found 20")
	else:
		print("Did not find 20")
	print("Finding Maximum")
	print("The max is {}".format(t.findMax().payload))
	print("Finding Minimum")
	print("The min is {}".format(t.findMin().payload))
	
	"""
	t.display()
	print("Removing from Tree 6")	
	t.deleteFromTree(6)
	"""

