class Bicycle(object):
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost
	
	
class BikeShop(object):

	inventory = []
	
	def __init__(self, name, inventory):
		self.name = name
		self.inventory = inventory
	
	margin = 0
	profit = 0
	
	def bike_price(self, cost):
		price = (1 + self.margin) * cost
		return bike_price
	
	def sell_bike(self, bike_name, price):
		self.profit = self.profit + (price - (price/(1+self.margin)))
		self.inventory[bike_name] = self.inventory[bike_name] - 1
		
class BikeCustomer(object):
	def __init__(self, name, budget, bike_owned):
		self.name = name
		self.budget = budget
		self.bike_owned = bike_owned
	
	def buy_bike(self, bike_name, price):
		self.bike_owned = bike_name
		self.budget = self.budget - price
		
	