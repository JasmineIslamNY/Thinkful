class OutputJSON (object):
	def __init__(self, dataobject):
		self.dataObject = dataobject
		self.json = "{\""

		self.returnOutput()

	def prepareOutput(self, data, parentIsAList="no"):
		count = 0
		while data.nextReturnPair <> None:
			if count > 0 and parentIsAList == "yes":
				self.json = self.json + ", "
				count += 1
			elif count > 0:
				self.json = self.json + ", \""
				count += 1
			else:
				count += 1

        		pair = data.returnNextPair()

			if pair.kind == "single":	
				self.json = self.json + pair.key + "\": \"" + pair.value + "\""
        		elif pair.kind == "list":
				self.json = self.json + pair.name + "\": [ "
				self.prepareOutput(pair, "yes")
			elif pair.kind == "group" and parentIsAList == "yes":
				self.json = self.json + " { \""
				self.prepareOutput(pair)	
			elif pair.kind == "group":
				self.json = self.json + pair.name + "\": { \""
				self.prepareOutput(pair)
			
		if data.kind == "list":
			self.json = self.json + " ]"
		elif data.kind == "group":
			self.json = self.json + " }"
		elif data.kind == "default":
			self.json = self.json + "}"
       
	def returnOutput(self):
		self.prepareOutput(self.dataObject)
