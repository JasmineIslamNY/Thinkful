from bicycle import * 

#initializing bikes
buster = Bicycle("Buster", 75, 100)
manx = Bicycle("Manx", 70, 150)
shadow = Bicycle("Shadow", 60, 300)
storm = Bicycle("Storm", 50, 600)
wallaby = Bicycle("Wallaby", 25, 800)
zeus = Bicycle("Zeus", 15, 2000)

jasmines_stock = [[buster, 10], [manx, 20], [shadow, 5], [storm, 5], [wallaby, 10], [zeus, 1]]

#initializing shop
shop = BikeShop("Jasmines Bike Shop", jasmines_stock)
shop.margin = .20

#initializing customers
john = BikeCustomer("John Smith", 200, "none")
sally = BikeCustomer("Sally Lions", 500, "none")
link = BikeCustomer("Link Bait", 1000, "none") 

""" Testing 
# this works to print the attributes of the bicycle objects
for item in shop.inventory:
	print item[0].name, item[0].weight, item[0].cost

# this gives the bike name and selling price
for item in shop.inventory:
	print item[0].name, shop.bike_price(item[0].cost)
	
 Testing """
#print the bikes the customers can afford
customers = [john, sally, link]
for customer in customers:
	print "These are the bikes that {} can afford:".format(customer.name)
	for item in shop.inventory:
		if (shop.bike_price(item[0].cost)) < customer.budget:
			print "Bike Model: {} Price: ${}".format(item[0].name, shop.bike_price(item[0].cost))
	print " "
# print bike shop inventory before customers buy bikes
print "{} has: ".format(shop.name)
for item in shop.inventory:
	print "{} {}'s ".format(item[1], item[0].name),
print " "
print " "

	
# each customer buys a bike they can afford
def cust_buys(customer, bike, price):
	print "{} has ${} in the bank".format(customer.name, customer.budget)
	customer.buy_bike(bike, price)
	shop.sell_bike(bike, price)
	print "{} just bought a {} for ${}!".format(customer.name, customer.bike_owned, price)
	print "{} now has ${} in the bank.".format(customer.name, customer.budget)
	print " "
	
cust_buys(john, "Buster", 120)
cust_buys(sally, "Shadow", 360)
cust_buys(link, "Wallaby", 960)

# print bike shop inventory after customers buy bikes and how much profit it made
print "{} now has: ".format(shop.name)
for item in shop.inventory:
	print "{} {}'s ".format(item[1], item[0].name),
print " "
print "{} made ${} in profit!".format(shop.name, shop.profit)
print " "