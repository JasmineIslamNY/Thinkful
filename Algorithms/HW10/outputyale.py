class OutputYALE (object):
	def __init__(self, dataobject):
		self.dataObject = dataobject
		self.IA = "" 
		self.A = ""
		self.JA = ""
		self.IACount = -1
		self.firstFlag = 0
		self.justAComma = ""
		self.returnYaleText = ""
	
		self.columns = -1

		self.returnOutput()
		self.IA = self.IA + self.justAComma + str((self.IACount+1))
		self.returnYale()

	def prepareOutput(self, data):
		while data.nextReturnPair <> None:

        		pair = data.returnNextPair()

			if pair.kind == "single":
				if pair.value != "0":
					self.IACount += 1
					self.A = self.A + self.justAComma + pair.value 
					self.JA = self.JA + self.justAComma + str(self.columns)
					if self.firstFlag == 0:
					    self.firstFlag = 1
					    self.IA = self.IA + self.justAComma + str(self.IACount)
					self.justAComma =", "
    			elif pair.kind == "list":
				self.columns = -1		
				self.firstFlag = 0
				self.prepareOutput(pair)
			elif pair.kind == "group":
				self.columns += 1
				self.prepareOutput(pair)
       
	def returnOutput(self):
		self.prepareOutput(self.dataObject)

	def returnYale(self):
		self.returnYaleText = "A: " + self.A + "\n" + "IA: " + self.IA + "\n" + "JA: " + self.JA
		