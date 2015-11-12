class OutputJSON (object):
	def __init__(self, dataobject):
		self.dataObject = dataobject
		self.json = "{ \""

		self.returnOutput()

	def readyOutput(self, data, isList, isGroup):
		count = 0
		while data.nextReturnPair <> None:
			if count > 0:
				self.json = self.json + ", \""
				count += 1
			else:
				count += 1

        		pair = data.returnNextPair()

			if pair.isList == "no" and pair.isGroup == "no":
				self.json = self.json + pair.key + "\": \"" + pair.value + "\""

        		elif pair.isList == "yes":
				self.json = self.json + pair.key + "\": [ { \""
				self.readyOutput(pair.value, "yes", "no")

			elif pair.isGroup == "yes":
				self.json = self.json + pair.key + "\": { \""
				self.readyOutput(pair.value, "no", "yes")	
			
		if isList == "no" and isGroup == "no":
			self.json = self.json + "}"
		if isList == "yes":
			self.json = self.json + " } ]"
		if isGroup == "yes":
			self.json = self.json + " }"
       
	def returnOutput(self):
		self.readyOutput(self.dataObject, "no", "no")