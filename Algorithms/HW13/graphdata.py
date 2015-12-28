class Node(object):
	def __init__(self, name):
		self.name = name
		self.edges = {}
	def addEdge(self, distance, toCity):
		self.edges[toCity] = distance

class GraphData(object):
	def __init__(self):
		self.list = []
	