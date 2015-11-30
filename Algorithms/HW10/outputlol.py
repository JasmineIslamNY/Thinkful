class OutputLOL (object):
	def __init__(self, dataobject):
		self.dataObject = dataobject
		self.lol = []
		self.returnListOfListText = ""
		self.columns = -1
		self.rows = -1

		self.returnOutput()
		self.columns +=1  #to setup the count of columns for humans
		addColumnText = "cols: " + str(self.columns)
		self.lol.insert(0, addColumnText)
		self.prepareListOfList()

	def prepareOutput(self, data):
		while data.nextReturnPair <> None:
			pair = data.returnNextPair()
		    
			if pair.kind == "single":
         			if pair.value != "0":
           				entry = "{" + str(self.columns) + "," + pair.value + "}"
           				self.lol[self.rows].append(entry) 
      			elif pair.kind == "list":
				self.columns = -1		
				self.rows += 1
				tempList = []
				self.lol.append(tempList) 
				listEntry = self.prepareOutput(pair)
			elif pair.kind == "group":
				self.columns += 1
				self.prepareOutput(pair)

       
	def returnOutput(self):
		self.prepareOutput(self.dataObject)

	def prepareListOfList(self):
		self.returnListOfListText = "LOL = " + str(self.lol)
