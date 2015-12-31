import random

def randomLots():
	result = random.randint(0,1)
	if result == 0:
		return 'No'
	else:
		return 'Yes'

def randomLogin():
	result = random.randint(0,1)
	if result == 0:
		return 'No'
	else:
		return 'Yes'

def randomWLSyncType():
	choices = ["server", "device", "merge"]
	result = random.choice(choices)
	return result

def randomCurrency():
	choices = ["Brazilian Real", "Euro", "Israeli Shekel", "Japanese Yen", "Malaysian Ringgit", "Singapore Dollar", "South Korean Won", "Turkish Lira", "US Dollar"] 
	result = random.choice(choices)
	return result

def randomSpreadsheetRow():
	result = random.randint(0,10000)	
	return result
	
def randomPrice():
	result = random.uniform(0,10000)	
	return result

def priceGrowth():
	result = random.uniform(0,100)	
	return result

def randomPosition():
	result = random.randint(0,10000)	
	return result
	
def positionGrowth():
	result = random.uniform(0,100)	
	return result

if __name__ == "__main__":
	print("Lots {}".format(randomLots()))
	print("Login {}".format(randomLogin()))
	print("SyncType {}".format(randomWLSyncType()))
	print("Currency {}".format(randomCurrency()))
	print("SpreadsheetRow {}".format(randomSpreadsheetRow()))
	print("RandomPrice {0:.2f}".format(randomPrice()))
	print("PriceGrowth {0:.2f}".format(priceGrowth()))
	print("RandomPosition {}".format(randomPosition()))
	print("PositionGrowth {0:.2f}".format(positionGrowth()))