from dataobject import DataObject

class InputXML(object):
	def __init__(self, input):
		self.input = input
		self.specialCharacters = ('<', '>', '/')
		self.processedInput = None
		
		self.processIt()

	def processInput(self, textData, tracker = "", tempKey = ""):
		parent = DataObject()
		tempValue = ""
		#tracker options include "", creatingKey, completedKey, creatingValue, creatingGroup, creatingList
		groupListEndTracker = None
		possibleGroupKey = ""
		possibleListKey = ""

		
		for i in range (1, len(textData)):
			if groupListEndTracker == "group":
				if textData[(i-len(possibleGroupKey)-2):i] == "</"+ possibleGroupKey +">":
					groupListEndTracker = None
			elif groupListEndTracker == "list":
				if textData[i] == "]":
					groupListEndTracker = None
			elif textData[i] in self.specialCharacters:
				if textData[i] == '<':
					if tracker == "":
						tracker = "creatingKey"
					elif tracker == "creatingKey":
						print('ERROR: Invalid <')
					elif tracker == "completedKey":

						
						tracker = "creatingValue"
					elif tracker == "creatingValue":
						tracker = ""
						parent.addKeyValue(tempKey, tempValue)
						tempKey = ""
						tempValue = ""	
					else:
						print('ERROR: Invalid "')

				if textData[i] == '>':
					if tracker == "":
						tracker = "creatingKey"
					elif tracker == "creatingKey":
						tracker = "completedKey"
					elif tracker == "completedKey":
						tracker = "creatingValue"
					elif tracker == "creatingValue":
						tracker = ""
						parent.addKeyValue(tempKey, tempValue)
						tempKey = ""
						tempValue = ""	
					else:
						print('ERROR: Invalid "')



				elif textData[i] == "{":
					groupListEndTracker = "group"
					child = self.processInput(textData[i:])
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
					child = self.processInput(textData[i:], "creatingList", tempKey)
					child.kind = "list"
					if tracker == "completedKey":
						tracker = ""
					child.name = tempKey
					tempKey = ""
					parent.addPair(child)
				elif textData[i] == "]":
					return parent

			else:
				if tracker == "creatingKey":
					tempKey = tempKey + textData[i]
				elif tracker == "creatingValue":
					tempValue = tempValue + textData[i]     #+ "*"
		return parent

	def processIt(self):
		self.processedInput = self.processInput(self.input)