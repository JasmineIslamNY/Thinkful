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


		i = 0
		while i < len(textData):
			if textData[i] in self.specialCharacters:
				if textData[i] == '<':
					if tracker == "":
						if textData[i:i+2] == '</':
							if textData[i:(i+len(tempListKey)+3)] == "</"+ tempListKey +">":
								parent.kind = "list"
								parent.name = tempListKey
								#print("i before {}".format(i))
								#print("what is tempListKey: {}".format(tempListKey))
								i= i + len(tempListKey) + 2	#there is an i increment by 1 at the bottom
								#print("i after {}".format(i))
								self.counter = i
								return parent
							elif textData[i:(i+len(tempGroupKey)+3)] == "</"+ tempGroupKey +">":
								#print("Using 2")
								parent.kind = "group"
								parent.name = tempGroupKey
								#print("i before {}".format(i))
								#print("what is tempGroupKey: {}".format(tempGroupKey))
								i= i + len(tempGroupKey) + 2	#there is an i increment by 1 at the bottom
								#print("i after {}".format(i))
								self.counter = i
								return parent
						else:
							#print("Using 3")
							tracker = "creatingKey"
					elif tracker == "creatingValue":
						if textData[i:i+2] == '</':
							if textData[i:(i+len(tempKey)+3)] == "</"+ tempKey +">":
								#print("Using 4")
								tracker = ""
								parent.addKeyValue(tempKey, tempValue)
								#print("i before {}".format(i))
								#print("what is tempKey: {}".format(tempKey))
								i = i + len(tempKey) + 2      #there is an i increment by 1 at the bottom 
								#print("i after {}".format(i))
								tempKey = ""
								tempValue = ""	
						elif textData[i:i+2] != '</' and tempGroupKey != "":
							#print("Using 5")
							#print(textData[i:])
							#print("******")	
							childObject = InputXML(textData[i:], tempKey)
							child = childObject.processedInput
							tempKey = ""
							tracker = ""
							if child.kind == "group":
								#print("Using 6")
								if self.previousGroupKey != "" and self.previousGroupKey != child.name:
									self.previousGroupKey = child.name
								elif self.previousGroupKey == "":
									self.previousGroupKey = child.name
								elif self.previousGroupKey == child.name:
									tempListKey = tempGroupKey
							#print("i before {}".format(i))
							#print("what is childObject.counter: {}".format(childObject.counter))
							i = i + childObject.counter
							#print("i after {}".format(i))
							parent.addPair(child)
						elif textData[i:i+2] != '</':
							#print("Using 7")
							#print(textData[i:])
							#print("******")	
							tempGroupKey = tempKey
							tempKey = ""
							tracker = ""
							#print("i before {}".format(i))
							i -= 1  		#this is to reset the count so the < is looked at again	
							#print("i after {}".format(i))					
				if textData[i] == '>':
					#print("Using 8")
					if tracker == "creatingKey":
						#print("Using 9")
						tracker = "creatingValue"	

			else:
				if tracker == "creatingKey":
					#print("Using 10")
					tempKey = tempKey + textData[i]
				elif tracker == "creatingValue":								
					#print("Using 11")
					tempValue = tempValue + textData[i]     #+ "*"
			i += 1
		self.counter = i
		return parent

	def processIt(self):
		self.processedInput = self.processInput(self.input)