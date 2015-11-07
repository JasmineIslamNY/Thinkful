from stack import Stack
from queue import Queue
from shunting import Shunting
from processOperators import operatorMath

class ReversePolishNotation(object):
	def __init__(self, input):
		self.inputQueue = input
		self.outputStack = Stack()
		self.operators = ["^", "*", "/", "%", "//", "+", "-", "(", ")"]
		
		print(self.inputQueue.peek())
		self.rpn()
	
	def rpn(self):
		while self.inputQueue.peek() <> []:
			holdItem = ""
			holdItem = self.inputQueue.dequeue()
	
			if holdItem in self.operators:
				operator2 = self.outputStack.pop()
				operator1 = self.outputStack.pop()
				result = operatorMath(operator1, holdItem, operator2)
				print(result)
				self.outputStack.push(result)
			else:
				self.outputStack.push(holdItem)

		

	
	
if __name__ == "__main__":
	Dijkstra = Shunting("3+4")
	print(Dijkstra.outputQueue.peek())
	Polish = ReversePolishNotation(Dijkstra.outputQueue)
	print(Polish.outputStack.peek())

	Dijkstra = Shunting("3+4*2/(1-5)^2^3")
	print(Dijkstra.outputQueue.peek())
	Polish = ReversePolishNotation(Dijkstra.outputQueue)
	print(Polish.outputStack.peek())






