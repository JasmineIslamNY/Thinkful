from dataobject import DataObject

class InputXML(object):
	def __init__(self, input):
		self.input = input
		self.specialCharacters = ('<', '>', '/')
		self.processedInput = None
		
		self.processIt()

	def processInput(self, textData, tempGroupKey = ""):
		parent = DataObject()
		tempKey = ""
		tempValue = ""
		tracker = ""
		#tracker options include "", creatingKey, completedKey, creatingValue, creatingGroup, creatingList
		groupListEndTracker = None
		tempListKey = ""
		previousGroupKey = ""

		i = 1
		while i < len(textData):
			if groupListEndTracker == "group":
				if textData[(i-len(tempGroupKey)-2):i] == "</"+ tempGroupKey +">":
					groupListEndTracker = None
			elif groupListEndTracker == "list":
				if textData[i] == "]":
					groupListEndTracker = None
			elif textData[i] in self.specialCharacters:
				if textData[i] == '<':
					if tracker == "":
						if textData[i:i+2] == '</':
							if textData[i:(i+len(tempListKey)+3)] == "</"+ tempListKey +">":
								parent.kind = "list"
								return parent
							elif textData[i:(i+len(tempGroupKey)+3)] == "</"+ tempGroupKey +">":
								parent.kind = "group"
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
					elif tracker == "completedKey":
						if textData[i:i+2] != '</':
							child = self.processInput(textData[i:])
							if child.kind == "group":
								if parent.previousGroupKey == "":
									parent.previousGroupKey = child.name
								elif parent.previousGroupKey == child.name
									parent.kind = "list"
									tempListKey = tempGroupKey
							parent.addPair(child)
				if textData[i] == '>':
					if tracker == "creatingKey":
						tracker = "creatingValue"	
					else:
						print('ERROR: Invalid >')



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
			i += 1
		return parent

	def processIt(self):
		self.processedInput = self.processInput(self.input)