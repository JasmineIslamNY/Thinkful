class OutputDOK (object):
	def __init__(self, dataobject):
		self.dataObject = dataobject
		self.dok = {}
		self.returnDictionaryText = ""
		self.rows = -1
		self.columns = -1

		self.returnOutput()
		self.rows +=1   #to setup the count of rows for humans
		self.columns +=1  #to setup the count of columns for humans
		self.dok['rows'] = self.rows
		self.dok['columns'] = self.columns
		self.returnDOK()

	def prepareOutput(self, data):
		while data.nextReturnPair <> None:

        		pair = data.returnNextPair()

			if pair.kind == "single":
				if pair.value != "0":
					dictKey = str(self.rows) + ":" + str(self.columns)	
					self.dok[dictKey] = pair.value
        		elif pair.kind == "list":
				self.columns = -1
				self.rows += 1				
				self.prepareOutput(pair)
        		elif pair.kind == "group":
				self.columns += 1
				self.prepareOutput(pair)
       
	def returnOutput(self):
		self.prepareOutput(self.dataObject)

	def returnDOK(self):
		self.returnDictionaryText = 'DOK = {' + "'rows':" + str(self.rows) + ", " + "'columns':" + str(self.columns)
		for keys, values in self.dok.items():
			if (keys != "rows"):
				if (keys != "columns"):
					self.returnDictionaryText = self.returnDictionaryText + ", " 
					self.returnDictionaryText = self.returnDictionaryText + "'" + keys + "':" + str(values)
		self.returnDictionaryText = self.returnDictionaryText + "}"
