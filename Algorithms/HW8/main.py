from shunting import Shunting
from reversepolishnotation import ReversePolishNotation
from processOperators import convertToString

class Main(object):
	def __init__(self):
		self.interim = ""
		self.solution = ""
		self.display_problem = ""

	def calculate(self, rawinput):
		input = rawinput.replace(" ", "")
		Dijkstra = Shunting(input)
		self.display_problem = rawinput
		temp = Dijkstra.outputQueue.peek()
		self.interim = convertToString(temp)

		Polish = ReversePolishNotation(Dijkstra.outputQueue)
		temp = Polish.outputStack.peek()
		self.solution = convertToString(temp)


