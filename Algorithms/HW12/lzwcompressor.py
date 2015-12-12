from binarytodecimal import binaryToDecimal
from decimaltobinary import decimalToBinary


class lzwCompressor(object):
	def __init__(self):
		self.compressed = ""
		self.size = 5
		self.dictionary = {}
		self.nextNumber = 0
		self.dictionarySeed = ["#","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
					"O","P","Q","R","S","T","U","V","W","X","Y","Z"]

		self.binaryObject = decimalToBinary()		#IS THIS A VALID USE????

	def inputCompress(self, input):
		self.size = 5
		self.nextNumber = 0
		self.generateDictionary(self.size)

		i = 0
		tracker = 1

		while i < len(input):
			tempInputSection = input[i:i+tracker]

			try:
				tempResult = self.dictionary[tempInputSection]
			except KeyError:
				tempResult = 0

			if tempInputSection == "#":
				self.compressed = self.compressed + "00000"
				return self.compressed
			elif tempResult != 0:  
				tracker += 1
			else:
				tracker -= 1
				tempInputSection2 = input[i:i+tracker]
				tempResult = self.dictionary[tempInputSection2]
	        		while len(tempResult) < self.size:
            				tempResult = "0" + tempResult		#to pad tempResult once size of db entries grow
				self.compressed = self.compressed + tempResult
				i = i + tracker
				tracker = 1
				self.addToDictionary(tempInputSection)		#moved this to bottom to take care of changing the width after adding current code
		

	def addToDictionary(self, inputSection):	
		newBinary = self.binaryObject.convert(self.nextNumber, self.size) 
		if len(newBinary) > self.size:
			self.size = len(newBinary)
		self.dictionary[inputSection] = newBinary		
		self.nextNumber += 1


	def generateDictionary(self, binSize):
		for member in self.dictionarySeed:
			binary = self.binaryObject.convert(self.nextNumber, binSize)
			self.dictionary[member] = binary
			self.nextNumber += 1

if __name__ == "__main__":
	test = lzwCompressor()
	dict = test.inputCompress('TOBEORNOTTOBEORTOBEORNOT#')
	print(dict)