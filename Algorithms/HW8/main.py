from shunting import Shunting
from reversepolishnotation import ReversePolishNotation

class Main(object):
	def __init__(self):
		self.interim = []
		self.solution = []
		self.display_problem = ""

	def calculate(self, input):
		Dijkstra = Shunting(input)
		self.display_problem = input
		self.interim = Dijkstra.outputQueue.peek()

		Polish = ReversePolishNotation(Dijkstra.outputQueue)
		self.solution = Polish.outputStack.peek()


