from binarytodecimal import binaryToDecimal
from decimaltobinary import decimalToBinary


class lzwDeCompressor(object):
	def __init__(self):
		self.deCompressed = ""
		self.size = 5
		self.reverseDictionary = {}
		self.nextNumber = 0
		self.nextBinary = ""
		self.previousCharacter = ""
		self.previousAdd = ""
		self.padCounter = 0
		self.dictionarySeed = ["#","A","B","C","D","E","F","G","H","I","J","K","L","M","N",
					"O","P","Q","R","S","T","U","V","W","X","Y","Z"]

		self.binaryObject = decimalToBinary()		#IS THIS A VALID USE????

	def inputDeCompress(self, input):
		self.size = 5
		self.nextNumber = 0
		self.generateReverseDictionary(self.size)

		i = 0
		tracker = 1

		while i < len(input):
			currentBinaryCharacter = input[i:i+self.size]				
			currentCharacter = self.retrieveFromReverseDictionary(currentBinaryCharacter, self.padCounter)
			if currentCharacter == 0:
				currentCharacter = self.previousAdd + self.previousAdd[0]
			elif currentCharacter == "#":
				self.deCompressed = self.deCompressed + "#"
				return self.deCompressed
			self.deCompressed = self.deCompressed + currentCharacter

			self.addToReverseDictionary(self.previousCharacter + currentCharacter[0])
			self.previousAdd = self.previousCharacter + currentCharacter[0]

			self.previousCharacter = currentCharacter


			i = i + self.size									#increment i before incrementing self.size for the next character

			self.nextBinary = self.binaryObject.convert(self.nextNumber, self.size) 		#increment it here so self.size is incremented before next character

			if len(self.nextBinary) > self.size:
				self.size = len(self.nextBinary)
				self.padCounter += 1
			self.nextNumber += 1

	def addToReverseDictionary(self, inputCharacter):	
		self.reverseDictionary[self.nextBinary] = inputCharacter

	def retrieveFromReverseDictionary(self, binaryCharacter, counter):
		try:
			tempCharacter = self.reverseDictionary[binaryCharacter]
		except KeyError:
			if counter == 0:
				return 0
			else:
				counter -= 1
				temp = binaryCharacter[1:]
				child = self.retrieveFromReverseDictionary(temp, counter)
				return child
		else:
			return tempCharacter	

	def generateReverseDictionary(self, binSize):
		for member in self.dictionarySeed:
			binary = self.binaryObject.convert(self.nextNumber, binSize)
			self.reverseDictionary[binary] = member
			self.nextNumber += 1

if __name__ == "__main__":
	test = lzwDeCompressor()
	dict = test.inputDeCompress("10100011110001000101011111001000111000111101010001101101110101111110010001111010000010001000000")
	print(dict)