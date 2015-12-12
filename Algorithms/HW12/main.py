from lzwcompressor import lzwCompressor

class Main(object):
	def __init__(self):
		self.output = ""
		self.input = ""

	def processInput(self, input):
		self.input = input

		process = lzwCompressor()
		self.output = process.inputCompress(input)
