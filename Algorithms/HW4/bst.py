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
			
	def deleteFromTree(self, value):
		if self.count == 0:
			return "Empty Tree"
		else:
			if self.root.payload == value:
				if self.root.leftNode != None:
					if self.root.rightNode != None:	
						self.addNodeToTree(self.root.rightNode, self.root.leftNode)
				else:
					self.root = self.root.leftNode
				if self.root.rightNode != None:
					self.root = self.root.rightNode  				
			elif value < self.root.payload:
				self.deleteFromChildTree(self.root, self.root.leftNode, value)
			else:
				self.deleteFromChildTree(self.root, self.root.rightNode, value)

	def deleteFromChildTree(self, parentTree, treeToDelete, value):
		if treeToDelete == None:
			return -1
		elif treeToDelete.payload == value:
			self.deleteTree(parentTree, treeToDelete)
		elif value < treeToDelete.payload:
			self.deleteFromChildTree(treeToDelete, treeToDelete.leftNode, value)
		else:
			self.deleteFromChildTree(treeToDelete, treeToDelete.rightNode, value)				

	def deleteTree(self, parentTree, treeToDelete):
		holdTree = None
		if treeToDelete.leftNode != None:
				if treeToDelete.rightNode != None:	
					self.addNodeToTree(treeToDelete.rightNode, treeToDelete.leftNode)
				else:
					holdTree = treeToDelete.leftNode
		if treeToDelete.rightNode != None:
				holdTree = treeToDelete.rightNode  
		treeToDelete.leftNode = None
		treeToDelete.rightNode = None
		# had to do this rather than just assigning holdTree to treeToDelete
		if treeToDelete.payload < parentTree.payload:
			parentTree.leftNode = holdTree
		else:
			parentTree.rightNode = holdTree
		#treeToDelete = holdTree



	"""
	def deleteTree(self, treeToDelete):
		holdTree = None
		if treeToDelete.leftNode != None:
				if treeToDelete.rightNode != None:	
					self.addNodeToTree(treeToDelete.rightNode, treeToDelete.leftNode)
				else:
					holdTree = treeToDelete.leftNode
		if treeToDelete.rightNode != None:
				holdTree = treeToDelete.rightNode  
		print (holdTree.payload)
		print (treeToDelete.payload)
		treeToDelete.leftNode = None
		treeToDelete.rightNode = None
		treeToDelete = holdTree
		print (holdTree.payload)
		print (treeToDelete.payload)

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
	t.addToTree(34)
	t.addToTree(74)
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
	
	t.display()
	print("Removing from Tree 6")	
	t.deleteFromTree(6)
	t.display()
	print("Removing from Tree 1")	
	t.deleteFromTree(1)
	t.display()
	print("Removing from Tree 34")	
	t.deleteFromTree(34)
	t.display()
	print("Removing from Tree 7")	
	t.deleteFromTree(7)
	t.display()
	

