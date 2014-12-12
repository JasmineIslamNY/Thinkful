from bicycle import * 

#instantiating bikes
buster = Bicycle("Buster", 75, 100)
manx = Bicycle("Manx", 70, 150)
shadow = Bicycle("Shadow", 60, 300)
storm = Bicycle("Storm", 50, 600)
wallaby = Bicycle("Wallaby", 25, 800)
zeus = Bicycle("Zeus", 15, 2000)

#instantiating shop
jasmines_stock = [[buster, 10], [manx, 20], [shadow, 5], [storm, 5], [wallaby, 10], [zeus, 1]]
shop = BikeShop("Jasmine's Bike Shop", jasmines_stock)
shop.margin = .20

#instantiating customers
john = BikeCustomer("John Smith", 200, "none")
sally = BikeCustomer("Sally Lions", 500, "none")
link = BikeCustomer("Link Bait", 1000, "none") 
 
#print the bikes the customers can afford from the bike shop
john.bike_options(shop)
sally.bike_options(shop)
link.bike_options(shop)

# print bike shop inventory before customers buy bikes
shop.print_inventory()
	
# each customer buys a bike they can afford	from shop
john.buy_bike("Buster", 120, shop)
sally.buy_bike("Shadow", 360, shop)
link.buy_bike("Wallaby", 960, shop)

# print bike shop inventory after customers buy bikes and how much profit it made
shop.print_inventory()
shop.print_profit()