from dataobject import DataObject

class inputJSON(object):
	self __init__(self, input):
		self.input = input
		self.specialCharacters = ("/"", "{", "}", "[", "]", ",", ":")


	def processInput(self, textData):
		parent = DataObject()
		tempKey = ""
		tempValue = None
		tracker = None #options include, None, creatingKey, completedKey, creatingValue, completedValue, creatingList, completedList, creatingGroup, completedGroup
		
		for i in range (0, len(textData)):
			if textData[i] in self.specialCharacters:
				if textData[i] == "/"":
					if tracker == None:
						tracker = "creatingKey"
					elif tracker == "creatingKey":
						tracker = "completedKey"
					elif tracker == "completedKey":
						tracker = "creatingValue"
					elif tracker == "creatingValue":
						tracker = "completedValue"
						
		
			elif textData[i] == " ":
				if tempKey == "":
					if tempValue = None:
						pass
					else:
						tempValue = tempValue + textData[i]
				else:
					tempKey = tempKey + textData[i]
			






		return parent