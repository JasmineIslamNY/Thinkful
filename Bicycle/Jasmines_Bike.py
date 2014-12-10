from bicycle import * 

#initializing bikes
buster = Bicycle("Buster", 75, 100)
manx = Bicycle("Manx", 70, 150)
shadow = Bicycle("Shadow", 60, 300)
storm = Bicycle("Storm", 50, 600)
wallaby = Bicycle("Wallaby", 25, 800)
zeus = Bicycle("Zeus", 15, 2000)

jasmines_stock = [[buster, 5], [manx.name, 5], [shadow.name, 5], [storm.name, 5], [wallaby.name, 5], [zeus.name, 5]]

#initializing shop
shop = BikeShop("Jasmines Bike Shop", jasmines_stock)
shop.margin = .20

#initializing customers
john = BikeCustomer("John Smith", 200, "none")
sally = BikeCustomer("Sally Lions", 500, "none")
link = BikeCustomer("Link Bait", 1000, "none") 

#print the bikes John Smith can afford
print "These are the bikes that {} can afford:".format(john.name)

for item in shop.inventory:
	print item[0]
