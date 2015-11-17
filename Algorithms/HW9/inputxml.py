from dataobject import DataObject

class InputXML(object):
	def __init__(self, input, groupKey = ""):
		self.input = input
		self.groupKey = groupKey
		self.specialCharacters = ('<', '>', '/')
		self.processedInput = None
		self.counter = 0
		self.previousGroupKey = ""
		self.processIt()

	def processInput(self, textData):
		parent = DataObject()
		tempKey = ""
		tempValue = ""
		tracker = ""
		#tracker options include "", creatingKey, completedKey, creatingValue, creatingGroup, creatingList
		groupListEndTracker = None
		tempGroupKey = self.groupKey
		tempListKey = ""


		i = 1
		while i < len(textData):
			if textData[i] in self.specialCharacters:
				if textData[i] == '<':
					if tracker == "":
						if textData[i:i+2] == '</':
							if textData[i:(i+len(tempListKey)+3)] == "</"+ tempListKey +">":
								parent.kind = "list"
								i= i + len(tempListKey) + 3
								self.counter = i
								return parent
							elif textData[i:(i+len(tempGroupKey)+3)] == "</"+ tempGroupKey +">":
								parent.kind = "group"
								parent.name = tempGroupKey
								i= i + len(tempListKey) + 3
								self.counter = i
								return parent
						else:
							tracker = "creatingKey"
					elif tracker == "creatingValue":
						if textData[i:i+2] == '</':
							if textData[i:(i+len(tempKey)+3)] == "</"+ tempKey +">":
								tracker = ""
								parent.addKeyValue(tempKey, tempValue)
								i = i + len(tempKey) + 2      #there is an i increment by 1 at the bottom 
								tempKey = ""
								tempValue = ""	
						elif textData[i:i+2] != '</':
							childObject = InputXML(textData[i:], tempKey)
							child = childObject.processedInput
							tempKey = ""
							tracker = ""
							if child.kind == "group":
								if self.previousGroupKey != "" and self.previousGroupKey != child.name:
									self.previousGroupKey = child.name
								elif self.previousGroupKey == "":
									self.previousGroupKey = child.name
								elif self.previousGroupKey == child.name:
									tempListKey = tempGroupKey
							i = i + childObject.counter
							parent.addPair(child)
				if textData[i] == '>':
					if tracker == "creatingKey":
						tracker = "creatingValue"	
					else:
						print('ERROR: Invalid >')

			else:
				if tracker == "creatingKey":
					tempKey = tempKey + textData[i]
				elif tracker == "creatingValue":
					tempValue = tempValue + textData[i]     #+ "*"
			i += 1
		self.counter = i
		return parent

	def processIt(self):
		self.processedInput = self.processInput(self.input)