class BikeShop(object):
	"""BikeShop needs a list called 'inventory' which should be comprised of bicycle objects and a count of bikes owned
	arguments for BikeShop are name and inventory, and methods include
	bike_price (cost of the bike) & sell_bike (real bike name and price) & update_inventory (real name of bike) & print_inventory
	and print_profit"""
	
	def __init__(self, name, inventory):
		self.name = name
		self.inventory = inventory
	
	margin = 0
	profit = 0
	
	def bike_price(self, cost):
		price = (1 + self.margin) * cost
		return price
				
	def sell_bike(self, bike_name, price):
		""" include the real name of the bike and the price """
		self.profit = self.profit + (price - (price/(1+self.margin)))
		self.update_inventory(bike_name)
		
	def update_inventory(self, bike_name):
		""" real name of the bike"""
		for item in self.inventory:
			if item[0].name == bike_name:
				item[1] -= 1
	
	def print_inventory(self):
		print "{} has: ".format(self.name)
		for item in self.inventory:
			print "{} {}'s ".format(item[1], item[0].name),
		print " "
		print " "
	
	def print_profit(self):
		print "{} made ${} in profit!".format(self.name, self.profit)
		print " "
	
class Bicycle(BikeShop):
	""" Bicycle need arguments name, weight, and cost """
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost
	
		
class BikeCustomer(BikeShop):
	"""BikeCustomer has name, budget, bike_owned and a method called buy_bike with bike_name and price"""
	def __init__(self, name, budget, bike_owned):
		self.name = name
		self.budget = budget
		self.bike_owned = bike_owned
	
	def buy_bike(self, bike_name, price, shopname):
	""" buy_bike takes bike_name (which is the actual name of the bike), and the price of the bike, and the bike shop it is being bought from """
		print "{} has ${} in the bank".format(self.name, self.budget)
		self.bike_owned = bike_name
		self.budget = self.budget - price
		shopname.sell_bike(bike_name, price)
		print "{} just bought a {} for ${} from {}!".format(self.name, self.bike_owned, price, shopname.name)
		print "{} now has ${} in the bank.".format(self.name, self.budget)
		print " "
		
	def bike_options(self, shopname):
		"""call with the name of the BikeShop you want the options from """
		print "These are the bikes that {} can afford from {}:".format(self.name, shopname.name)
		for item in shopname.inventory:
			if (shopname.bike_price(item[0].cost)) < self.budget:
				print "Bike Model: {} Price: ${}".format(item[0].name, shopname.bike_price(item[0].cost))
		print " "
		
		
