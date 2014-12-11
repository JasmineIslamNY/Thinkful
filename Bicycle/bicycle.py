class Bicycle(object):
	""" Bicycle need arguments name, weight, and cost """
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost
	
	
class BikeShop(object):
	"""BikeShop has a list called 'inventory', arguments name and inventory, and methods
	bike_price (self, cost) and sell_bike (bike_name, price) """
	
	def __init__(self, name, inventory):
		self.name = name
		self.inventory = inventory
	
	margin = 0
	profit = 0
	
	def bike_price(self, cost):
		price = (1 + self.margin) * cost
		return price
				
	def sell_bike(self, bike_name, price):
		self.profit = self.profit + (price - (price/(1+self.margin)))
		self.update_inventory(bike_name)
		
	def update_inventory(self, bike_name):
		for item in self.inventory:
			if item[0].name == bike_name:
				item[1] -= 1

		
class BikeCustomer(object):
	"""BikeCustomer has name, budget, bike_owned and a method called buy_bike with bike_name and price"""
	def __init__(self, name, budget, bike_owned):
		self.name = name
		self.budget = budget
		self.bike_owned = bike_owned
	
	def buy_bike(self, bike_name, price):
		self.bike_owned = bike_name
		self.budget = self.budget - price
		# BikeShop.sell_bike(bike_name, price)
		
	