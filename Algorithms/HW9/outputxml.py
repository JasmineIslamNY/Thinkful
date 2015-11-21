class OutputXML (object):
	def __init__(self, dataobject):
		self.dataObject = dataobject
		self.xml = ""

		self.returnOutput()

	def prepareOutput(self, data, parentIsAList="no"):
		self.xml = self.xml + "<" + data.name + ">"
		while data.nextReturnPair <> None:

        		pair = data.returnNextPair()

			if pair.kind == "single":	
				self.xml = self.xml + "<" + pair.key + ">" + pair.value + "</"+ pair.key + ">"
        		else:
				self.prepareOutput(pair)
			
		
		self.xml = self.xml + "</" + data.name + ">"
       
	def returnOutput(self):
		self.prepareOutput(self.dataObject)
