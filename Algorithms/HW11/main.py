from jasMurmur32 import JASMurmur32

class Main(object):
	def __init__(self):
		self.output = ""
		self.input = ""
		self.list = []

	def processInput(self, input):
		self.input = input
		self.list.append(input)
		hash = JASMurmur32(input)		

	

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