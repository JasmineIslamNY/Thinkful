class BST(object):
	def __init__(self, payload=None):
		self.count = 0
		self.root = None
		self.payload = payload
		self.leftTree = None
		self.rightTree = None
	

	def addToTree(self, value):
		tree = BST(value)
		if self.root == None:
			self.root = tree
			self.count += 1
		else:
			self.addTreeToTree(self.root, tree)
		
	def addTreeToTree(self, parent, child):
		if child.payload <= parent.payload:
			if parent.leftTree == None:
				parent.leftTree = child
				self.count += 1
			else:
				self.addTreeToTree(parent.leftTree, child)
		else:
			if parent.rightTree == None:
				parent.rightTree = child
				self.count += 1
			else:
				self.addTreeToTree(parent.rightTree, child)

	def findInTree(self, value):
		if self.count == 0:
			return -1
		else:
			if self.root.payload == value:
				return 1
			elif value < self.root.payload:
				self.findInChildTree(self.root.leftTree, value)
			else:
				self.findInChildTree(self.root.rightTree, value)

	def findInChildTree(self, tree, value):
		if tree == None:
			return -1
		elif tree.payload == value:
			return 1
		elif value < tree.payload:
			self.findInChildTree(tree.leftTree, value)
		else:
			self.findInChildTree(tree.rightTree, value)
			
	def deleteFromTree(self, value):
		if self.count == 0:
			return "Empty Tree"
		else:
			if self.root.payload == value:
				if self.root.leftTree == None and self.root.rightTree == None:
					self.root = None
					self.payload = None
					self.count = 0
				elif self.root.leftTree != None:
					if self.root.rightTree != None:	
						self.addTreeToTree(self.root.rightTree, self.root.leftTree)
						self.root = self.root.rightTree
						self.count -= 1 						
					else:
						self.root = self.root.leftTree
						self.count -= 1
				else:
					self.root = self.root.rightTree
					self.count -= 1  				
			elif value < self.root.payload:
				self.deleteFromChildTree(self.root, self.root.leftTree, value)
			else:
				self.deleteFromChildTree(self.root, self.root.rightTree, value)

	def deleteFromChildTree(self, parentTree, treeToDelete, value):
		if treeToDelete == None:
			return -1
		elif treeToDelete.payload == value:
			self.deleteTree(parentTree, treeToDelete)
		elif value < treeToDelete.payload:
			self.deleteFromChildTree(treeToDelete, treeToDelete.leftTree, value)
		else:
			self.deleteFromChildTree(treeToDelete, treeToDelete.rightTree, value)				

	def deleteTree(self, parentTree, treeToDelete):
		holdTree = None
		if treeToDelete.leftTree != None:
				if treeToDelete.rightTree != None:	
					self.addTreeToTree(treeToDelete.rightTree, treeToDelete.leftTree)
				else:
					holdTree = treeToDelete.leftTree
		if treeToDelete.rightTree != None:
				holdTree = treeToDelete.rightTree  
		treeToDelete.leftTree = None
		treeToDelete.rightTree = None
		# had to do this rather than just assigning holdTree to treeToDelete
		if treeToDelete.payload < parentTree.payload:
			parentTree.leftTree = holdTree
		else:
			parentTree.rightTree = holdTree
		#treeToDelete = holdTree
		self.count -= 1



	"""
	def deleteTree(self, treeToDelete):
		holdTree = None
		if treeToDelete.leftTree != None:
				if treeToDelete.rightTree != None:	
					self.addTreeToTree(treeToDelete.rightTree, treeToDelete.leftTree)
				else:
					holdTree = treeToDelete.leftTree
		if treeToDelete.rightTree != None:
				holdTree = treeToDelete.rightTree  
		print (holdTree.payload)
		print (treeToDelete.payload)
		treeToDelete.leftTree = None
		treeToDelete.rightTree = None
		treeToDelete = holdTree
		print (holdTree.payload)
		print (treeToDelete.payload)

	"""

	
	def display(self):					
		if (self.count == 0):
			print("Empty Tree")
		else:
			print(self.root.payload)
			self.displayChildTree(self.root.leftTree)
			self.displayChildTree(self.root.rightTree)
			
	def displayChildTree(self, tree):					
		if tree == None:
			return -1
		else:
			print(tree.payload)
			self.displayChildTree(tree.leftTree)
			self.displayChildTree(tree.rightTree)


	def findMax(self):
		if self.count == 0:
			return "Empty Tree"
		else:
			return self.findMaxInChild(self.root)

	
	def findMaxInChild(self, tree):
		if tree.rightTree == None:
			return tree
		else:
			return self.findMaxInChild(tree.rightTree)

	def findMin(self):
		if self.count == 0:
			return "Empty Tree"
		else:
			return self.findMinInChild(self.root)

	
	def findMinInChild(self, tree):
		if tree.leftTree == None:
			return tree
		else:
			return self.findMinInChild(tree.leftTree)
		

if __name__ == "__main__":
	t = BST()
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
	print("Number of entries in tree: {}".format(t.count))
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
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 1")	
	t.deleteFromTree(1)
	t.display()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 34")	
	t.deleteFromTree(34)
	t.display()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 7")	
	t.deleteFromTree(7)
	t.display()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 5")	
	t.deleteFromTree(5)
	t.display()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 34")	
	t.deleteFromTree(34)
	t.display()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 74")	
	t.deleteFromTree(74)
	t.display()
	print("Number of entries in tree: {}".format(t.count))	
	print("Removing from Tree 4")	
	t.deleteFromTree(4)
	t.display()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 74")	
	t.deleteFromTree(74)
	t.display()
