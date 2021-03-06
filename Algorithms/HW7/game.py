from stack import Stack

class Game(object):
	def __init__(self):
		self.tower1 = Stack()
		self.tower2 = Stack()
		self.tower3 = Stack()
		self.fromTower = None
		self.toTower = None
		self.moves = 0
				

		self.tower1.push(3)
		self.tower1.push(2)
		self.tower1.push(1)
	


	def printTower(self, towerNum):
		if towerNum.count == 0:
			return " "		
		else:
			list = towerNum.peek
			div = ""
			for i in range(0,towerNum.count):
				div = div + "<div class=disk id=disk" + str(i) + ">=</div> "
			return div
	
	def moveDisk(self, fromTwr, toTwr):
		toTowerValue = toTwr.peek()
		fromTowerValue = fromTwr.peek()
		if toTowerValue== []:
			toTowerValue = [100]

		if fromTwr.count == 0:
			return -1
		elif fromTowerValue[0] >= toTowerValue[0]:
			return -1
		else:
			toTwr.push(fromTwr.pop())

	def buttonPressed(self, button):
		if button == 'reset':
			self.resetGame()
		elif button == 'tower1':
			tower = self.tower1
			self.towerSelected(tower)
		elif button == 'tower2':
			tower = self.tower2
			self.towerSelected(tower)
		elif button == 'tower3':
			tower = self.tower3
			self.towerSelected(tower)
			
	def towerSelected(self, tower):
		if self.fromTower == None:
			self.fromTower = tower
		else:
			self.toTower = tower
			self.moveDisk(self.fromTower, self.toTower)
			self.toTower = None
			self.fromTower = None
			self.moves += 1

	def displayFromTower(self):
		if self.fromTower == self.tower1:
			return "Tower 1"
		elif self.fromTower == self.tower2:
			return "Tower 2"
		elif self.fromTower == self.tower3:
			return "Tower 3"

	def resetGame(self):
		self.tower1 = Stack()
		self.tower2 = Stack()
		self.tower3 = Stack()
		self.fromTower = None
		self.toTower = None
		self.moves = 0
				

		self.tower1.push(3)
		self.tower1.push(2)
		self.tower1.push(1)
	
if __name__ == "__main__":
	game = Game()
	game.tower1.push(3)
	game.tower1.push(2)
	game.tower1.push(1)
	print(game.printTower(game.tower1))
	print(game.printTower(game.tower2))
	print(game.printTower(game.tower3))
	game.moveDisk(game.tower1, game.tower2)
	print(game.printTower(game.tower1))
	print(game.printTower(game.tower2))
	print(game.printTower(game.tower3))
	game.moveDisk(game.tower3, game.tower1)
	print(game.printTower(game.tower1))
	print(game.printTower(game.tower2))
	print(game.printTower(game.tower3))	







