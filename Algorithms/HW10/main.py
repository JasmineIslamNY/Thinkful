from dataobject import DataObject
from outputjson import OutputJSON
from inputjson import InputJSON
from outputdok import OutputDOK
from outputlol import OutputLOL
from outputyale import OutputYALE

class Main(object):
	def __init__(self):
		self.dokOutput = ""
		self.lolOutput = ""
		self.yaleOutput = ""
		self.input = ""

	def processInput(self, input):
		self.input = input

		processed = InputJSON(input)		
		temp = OutputDOK(processed.processedInput)
		self.dokOutput = temp.returnDictionaryText
	
		processed = InputJSON(input)
		temp = OutputLOL(processed.processedInput)
		self.lolOutput = temp.returnListOfListText
		
		processed = InputJSON(input)
		temp = OutputYALE(processed.processedInput)
		self.yaleOutput = temp.returnYaleText

if __name__ == "__main__":
	
	yale_input = '{"row": [{"value":0},{"value":0},{"value":0},{"value":0}],"row": [{"value":5},{"value":8},{"value":0},{"value":0}],"row": [{"value":0},{"value":0},{"value":3},{"value":0}],"row": [{"value":0},{"value":6},{"value":0},{"value":0}]}'

	print("Original yale_input")
	print("-------------")
	print("             ")
	print(yale_input)
	print("             ")

	print("Processed JSON")
	print("-------------")
	print("             ")
	processed = InputJSON(yale_input)
	temp = OutputJSON(processed.processedInput)
	print(temp.json)
	print("             ")

	print("Processed DOK")
	print("-------------")
	print("             ")
	processed = InputJSON(yale_input)
	temp = OutputDOK(processed.processedInput)
	print(temp.returnDictionaryText)
	print("             ")

	print("Processed LOL")
	print("-------------")
	print("             ")
	processed = InputJSON(yale_input)
	temp = OutputLOL(processed.processedInput)
	print(temp.returnListOfListText)
	print("             ")

	print("Processed YALE")
	print("-------------")
	print("             ")
	processed = InputJSON(yale_input)
	temp = OutputYALE(processed.processedInput)
	print(temp.returnYaleText)
	print("             ")