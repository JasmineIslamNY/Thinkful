from jasMurmur32 import JASMurmur32
from randomText import randomText

class Main(object):
	def __init__(self):
		self.input = ""
		self.list = []
		self.bitVector = {}
		self.bitVectorDisplay = ""
		self.inclusionTest = ""
		
		self.loadBitVector(32)
		self.hashObject1 = JASMurmur32()
		self.hashObject2 = JASMurmur32(7748789268798787808)

	def processInput(self, input):
		self.inclusionTest = ""
		self.input = input
		self.list.append(input)

		hash1 = self.hashObject1.createHash(input)
		self.bitVector[hash1] += 1

		hash2 = self.hashObject2.createHash(input)
		self.bitVector[hash2] += 1
		
		self.bitVectorDisplay = ""
		for n in range(0,32):
			if self.bitVector[n] == 0:
				self.bitVectorDisplay = self.bitVectorDisplay + "0"
			else:
				self.bitVectorDisplay = self.bitVectorDisplay + "X"

	def loadBitVector(self, size=32):		
		for i in range(0, size):
			self.bitVector[i] = 0	
	
	def loadRandomWord(self, loopNumber=2):
		loopNumber = int(loopNumber)
		for i in range(0, loopNumber):
			wordObject = randomText()
			word = wordObject.createRandomWord()
			self.processInput(word)

	def checkBitVector(self, word):
		hash1 = self.hashObject1.createHash(word)	
		hash2 = self.hashObject2.createHash(word)
		print(hash1)
		print(hash2)
		
		if self.bitVector[hash1] == 0 and self.bitVector[hash2] == 0:
			return 0
		else:
			return 1

	def checkList(self, word):
		try:
			checkIndex = self.list.index(word)
		except ValueError:
			return 0
		else:
			return self.list[checkIndex]

	def testInclusion(self, word):
		result = self.checkBitVector(word)
		if result == 0:
			self.inclusionTest = "Value not in the set"
		else:
			result = self.checkList(word)
			if result == 0:
				self.inclusionTest = "False positive"
			else:
				self.inclusionTest = result + " found in the set"

	

if __name__ == "__main__":
	test = Main()
	test.processInput("Mary had a little lamb")
	test.processInput("Mary had a little lamb")
	test.processInput("his fleece was white as snow")
	test.processInput("And everywhere that Mary went")
	test.processInput("The lamb was sure to go")
	print(test.input)
	print(test.list)
	print(test.bitVector)
	print(test.inclusionTest)

	print("loading a random word")
	print("---------------------")

	test.loadRandomWord()
	print(test.input)
	print(test.list)
	print(test.bitVector)
	print(test.inclusionTest)

	print("test for inclusion - not in set")
	print("------------------")
	test.testInclusion("jrioeui299on djkffu1kljkeh fjkhoueiouu jfkdhjkbkje jkdhfjkdhfjkhjk dhfjhkj diuio hj 18903890 fj2909- 3kjklk  djeiop 3434456 $^%^*^&*&v%^*^%^&*  ^%&*%^&*%*$yuY GUTYGU")
	print(test.inclusionTest)
	print(" ")

	print("test for inclusion - in set")
	print("------------------")
	test.testInclusion("Mary had a little lamb")
	print(test.inclusionTest)
	print(" ")

	print("test for inclusion - false positive")
	print("------------------")
	test.testInclusion("Mary had a little la")
	print(test.inclusionTest)
	print(" ")
