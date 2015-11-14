from dataobject import DataObject

class inputJSON(object):
	self __init__(self, input):
		self.input = input
		self.specialCharacters = ("/"", "{", "}", "[", "]", ",", ":")
		
		self.processedInput = self.processInput(self.input)

	def processInput(self, textData, tracker = "", tempKey = ""):
		parent = DataObject()
		tempValue = None
		#tracker options include "", creatingKey, completedKey, creatingValue, creatingList
		groupListEndTracker = None
		
		for i in range (0, len(textData)):
			if groupListEndTracker == "group":
				if textData[i] == "}":
					groupListEndTracker = None
			elif groupListEndTracker == "list":
				if textData[i] == "]":
					groupListEndTracker = None
			elif textData[i] in self.specialCharacters:
				if textData[i] == "/"":
					if tracker == "":
						tracker = "creatingKey"
					elif tracker == "creatingKey":
						tracker = "completedKey"
					elif tracker == "completedKey":
						tracker = "creatingValue"
					elif tracker == "creatingValue":
						tracker = ""
						parent.addKeyValue(tempKey, tempValue)	
					else:
						print("ERROR: Invalid /"")
				elif textData[i] == "{":
					groupListEndTracker = "group"
					child = self.processInput(textData[i+1:])
					child.kind = "group"
					if tracker == "completedKey":
						tracker = ""
						child.name = tempKey
						tempKey = ""
						parent.addPair(child)
					elif tracker == "creatingList":
						groupName = tempKey + "_item"
						child.name = groupName
						parent.addPair(child)
				elif textData[i] == "}":
					return parent
				elif textData[i] == "[":
					groupListEndTracker = "list"
					child = self.processInput(textData[i+1:], "creatingList", tempKey)
					child.kind = "list"
					if tracker == "completedKey":
						tracker = ""
					child.name = tempKey
					tempKey = ""
					parent.addPair(child)
				elif textData[i] == "]":
					return parent
			elif textData[i] == " ":
				if tempKey == "":
					if tempValue = None:
						pass
					else:
						tempValue = tempValue + textData[i]
				else:
					tempKey = tempKey + textData[i]
			
			else:
				if tracker == "creatingKey":
					tempKey = tempKey + textData[i]
				elif tracker == "creatingValue":
					tempValue = tempValue + textData[i]
		return parent