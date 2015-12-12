from lzwcompressor import lzwCompressor
from lzwdecompressor import lzwDeCompressor

class Main(object):
	def __init__(self):
		self.output = ""
		self.input = ""
		self.label = ""

	def encodeInput(self, input):
		self.input = input
		countBeforeEncode = str(len(input) * 5)

		process = lzwCompressor()
		self.output = process.inputCompress(input)

		countAfterEncode = str(len(self.output))
		
		self.label = "Length before compression = " + countBeforeEncode + ". Length after compression = " + countAfterEncode + "."

	def decodeInput(self, input):
		self.label = ""
		self.input = input

		process = lzwDeCompressor()
		self.output = process.inputDeCompress(input)



if __name__ == "__main__":
	test = Main()
	encode = test.encodeInput('TOBEORNOTTOBEORTOBEORNOT#')
	print(test.output)
	print("10100011110001000101011111001000111000111101010001101101110101111110010001111010000010001000000 - to compare")

	decode = test.decodeInput('10100011110001000101011111001000111000111101010001101101110101111110010001111010000010001000000')
	print(test.output)
	print("TOBEORNOTTOBEORTOBEORNOT# - to compare")