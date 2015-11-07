from stack import Stack
from queue import Queue
from processOperators import compareOperators, operatorToNumber

class Shunting(object):
	def __init__(self, input):
		self.inputQueue = Queue()
		self.outputQueue = Queue()
		self.operatorStack = Stack()
		self.input = input
		self.operators = ["^", "*", "/", "%", "//", "+", "-", "(", ")"]
		
		self.processInput(self.input)
		print(self.inputQueue.peek())
		self.shunt()

	def processInput(self, input):
		holdItem = ""
		for i in range(0, len(input)):
			if input[i] in self.operators:
				if holdItem <> "":
					self.inputQueue.enqueue(holdItem)
				self.inputQueue.enqueue(input[i])
				holdItem = ""
			else:
				holdItem = holdItem + input[i]
		if holdItem <> "":
			self.inputQueue.enqueue(holdItem)
	
	def shunt(self):
		while self.inputQueue.peek() <> []:
			holdItem = ""
			holdItem = self.inputQueue.dequeue()
	
			if holdItem == "(":
				self.operatorStack.push(holdItem)
			elif holdItem == ")":
				temp = self.operatorStack.pop()
				while temp <> "(":
					self.outputQueue.enqueue(temp)
					temp = self.operatorStack.pop()
			elif holdItem in self.operators:
				if self.operatorStack.peek() == []:
					self.operatorStack.push(holdItem)
				else:
					while holdItem <> "":
						if self.operatorStack.peek() == []:
							self.operatorStack.push(holdItem)
							holdItem =""
						else:	
							result = compareOperators(holdItem, self.operatorStack.peek()[0])
							if result == 1:
								self.operatorStack.push(holdItem)
								holdItem = ""
							elif result == -1:
								self.outputQueue.enqueue(self.operatorStack.pop())

			else:
				self.outputQueue.enqueue(holdItem)

		while self.operatorStack.peek() <> []:
			self.outputQueue.enqueue(self.operatorStack.pop())

	
	
if __name__ == "__main__":
	Dijkstra = Shunting("3+4")
	print(Dijkstra.outputQueue.peek())
	Dijkstra = Shunting("3+4*2/(1-5)^2^3")
	print(Dijkstra.outputQueue.peek())

	Dijkstra = Shunting("3*4+2")
	print(Dijkstra.outputQueue.peek())






