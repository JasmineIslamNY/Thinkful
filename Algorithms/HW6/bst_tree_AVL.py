class BST(object):
	def __init__(self, payload=None):
		self.count = 0
		self.root = None
		self.payload = payload
		self.leftTree = None
		self.rightTree = None
		self.rightDepth = 0
		self.leftDepth = 0
	
	def isBalanced(self):
		#print("rightDepth is {}".format(self.rightDepth))
		#print("leftDepth is {}".format(self.leftDepth))
		if abs(self.rightDepth - self.leftDepth) > 1:
			return 'No'
		else:
			return 'Yes'

	def updateDepth(self, side, depth):
		if side == 'right':
			if depth > self.rightDepth:
				self.rightDepth = depth
		else:
			if depth > self.leftDepth:
				self.leftDepth = depth
	
	def balanceTree(self, side):
		if side == 'left':
			print("Rebalancing left")
			if self.findDepth(self.root.leftTree.rightTree) > (self.leftDepth - 1):
				newRight = self.root
				newLeft = self.root.leftTree
				newRoot = self.root.leftTree.rightTree
				newLeft.rightTree = newRoot.leftTree
				newRight.leftTree = newRoot.rightTree
				newRoot.leftTree = newLeft
				newRoot.rightTree = newRight
				self.root = newRoot
				print("LeftDepth before: {}".format(self.leftDepth))	
				self.leftDepth -= 1
				print("LeftDepth after: {}".format(self.leftDepth))
			else:
				oldRoot = self.root
				newRoot = self.root.leftTree
				oldRoot.leftTree = newRoot.rightTree
				newRoot.rightTree = oldRoot
				self.root = newRoot
				print("LeftDepth before: {}".format(self.leftDepth))	
				self.leftDepth -= 1
				print("LeftDepth after: {}".format(self.leftDepth))
		else:
			print("Rebalancing right")
			if self.findDepth(self.root.rightTree.leftTree) > (self.rightDepth - 1):
				newLeft = self.root
				newRight = self.root.rightTree
				newRoot = self.root.rightTree.leftTree
				newLeft.rightTree = newRoot.leftTree
				newRight.leftTree = newRoot.rightTree
				newRoot.leftTree = newLeft
				newRoot.rightTree = newRight
				self.root = newRoot
				print("RightDepth before: {}".format(self.rightDepth))	
				self.rightDepth -= 1
				print("RightDepth after: {}".format(self.rightDepth))
			else:
				oldRoot = self.root
				newRoot = self.root.rightTree
				oldRoot.rightTree = newRoot.leftTree
				newRoot.leftTree = oldRoot
				self.root = newRoot
				print("RightDepth before: {}".format(self.rightDepth))
				self.rightDepth -= 1
				print("RightDepth after: {}".format(self.rightDepth))

	def findDepth(self, tree):
		if tree == None:
			return 0
		elif (self.findDepth(tree.leftTree) > self.findDepth(tree.rightTree)):
			return (1 + self.findDepth(tree.leftTree))
		else:
			return (1 + self.findDepth(tree.rightTree))
		
	def addToTree(self, value):
		tree = BST(value)
		self.count += 1
		if self.root == None:
			self.root = tree
		else:
			self.addTreeToTree(self.root, tree)
		
	def addTreeToTree(self, parent, child, depth=0, side=None):
		if child.payload <= parent.payload:
			if parent.leftTree == None:
				parent.leftTree = child
				depth += 1
				if side == None:
					side = 'left'
				self.updateDepth(side, depth)
				#print("Added at depth: {}".format(depth))
				print("Is the tree balanced: {}".format(self.isBalanced()))
				balanced = self.isBalanced()
				if balanced == 'No':
					self.balanceTree(side)
			else:
				depth += 1
				if side == None:
					side = 'left'				
				self.addTreeToTree(parent.leftTree, child, depth, side)
		else:
			if parent.rightTree == None:
				parent.rightTree = child
				depth += 1
				if side == None:
					side = 'right'
				self.updateDepth(side, depth)
				#print("Added at depth: {}".format(depth))
				print("Is the tree balanced: {}".format(self.isBalanced()))
				balanced = self.isBalanced()
				if balanced == 'No':
					self.balanceTree(side)
			else:
				depth += 1
				if side == None:
					side = 'right'	
				self.addTreeToTree(parent.rightTree, child, depth, side)

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

	
	def preorder(self):					
		if (self.count == 0):
			print("Empty Tree")
		else:
			print(self.root.payload)
			self.preorderChildTree(self.root.leftTree)
			self.preorderChildTree(self.root.rightTree)
			
	def preorderChildTree(self, tree):					
		if tree == None:
			return -1
		else:
			print(tree.payload)
			self.preorderChildTree(tree.leftTree)
			self.preorderChildTree(tree.rightTree)

	def inorder(self):					
		if (self.count == 0):
			print("Empty Tree")
		else:
			self.inorderChildTree(self.root.leftTree)
			print(self.root.payload)
			self.inorderChildTree(self.root.rightTree)
			
	def inorderChildTree(self, tree):					
		if tree == None:
			return -1
		else:
			self.inorderChildTree(tree.leftTree)
			print(tree.payload)
			self.inorderChildTree(tree.rightTree)

	def postorder(self):					
		if (self.count == 0):
			print("Empty Tree")
		else:
			self.postorderChildTree(self.root.leftTree)
			self.postorderChildTree(self.root.rightTree)
			print(self.root.payload)
			
	def postorderChildTree(self, tree):					
		if tree == None:
			return -1
		else:
			self.postorderChildTree(tree.leftTree)
			self.postorderChildTree(tree.rightTree)
			print(tree.payload)

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
	#t.preorder()
	print("Adding in the following order: 7, 1, 6, 5, 34, 4, 34, 74, 31, 61")
	t.addToTree(7)
	t.addToTree(1)
	t.addToTree(6)
	t.addToTree(5)
	t.addToTree(34)
	t.addToTree(4)
	t.addToTree(34)
	t.addToTree(74)
	t.addToTree(31)
	t.addToTree(61)

	print("Print in pre-order")
	t.preorder()
	print("Print in in-order")
	t.inorder()
	print("Print in post-order")
	t.postorder()


	"""

	t.preorder()
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
	
	t.preorder()
	print("Removing from Tree 6")	
	t.deleteFromTree(6)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 1")	
	t.deleteFromTree(1)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 34")	
	t.deleteFromTree(34)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 7")	
	t.deleteFromTree(7)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 5")	
	t.deleteFromTree(5)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 34")	
	t.deleteFromTree(34)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 74")	
	t.deleteFromTree(74)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))	
	print("Removing from Tree 4")	
	t.deleteFromTree(4)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))
	print("Removing from Tree 74")	
	t.deleteFromTree(74)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))	
	print("Removing from Tree 31")	
	t.deleteFromTree(31)
	t.preorder()
	print("Number of entries in tree: {}".format(t.count))	
	print("Removing from Tree 61")	
	t.deleteFromTree(61)
	t.preorder()

	"""