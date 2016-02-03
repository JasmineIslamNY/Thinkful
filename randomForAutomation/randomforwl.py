import random

class RandomForWL(object):
	def __init__(self):
		self.temp = 0

	def randomLots(self):
		result = random.randint(0,1)
		if result == 0:
			return 'No'
		else:
			return 'Yes'

	def randomLogin(self):
		result = random.randint(0,1)
		if result == 0:
			return 'No'
		else:
			return 'Yes'

	def randomWLSyncType(self):
		choices = ["server", "device", "merge"]
		result = random.choice(choices)
		return result

	def randomCurrency(self):
		choices = ["Brazilian Real", "Euro", "Israeli Shekel", "Japanese Yen", "Malaysian Ringgit", "Singapore Dollar", "South Korean Won", "Turkish Lira", "US Dollar"] 
		result = random.choice(choices)
		return result

	def randomRow(self, rowSize=10000):
		result = random.randint(0, rowSize)	
		return result

	def randomResultLimit(self, limitSize=10):
		limitExponent = random.randint(0, limitSize)	
		limit = 10 ** limitExponent
		return limit
	
	def randomPrice(self, resultLimit=10000000000):
		result = random.uniform(0,resultLimit)	
		return result

	def priceGrowth(self):
		result = random.uniform(0,100)	
		return result

	def randomPosition(self, resultLimit=10000000000):
		result = random.randint(0,resultLimit)	
		return result
	
	def positionGrowth(self):
		result = random.uniform(0,100)	
		return result

if __name__ == "__main__":
	r = RandomForWL()
	print("Lots {}".format(r.randomLots()))
	print("Login {}".format(r.randomLogin()))
	print("SyncType {}".format(r.randomWLSyncType()))
	print("Currency {}".format(r.randomCurrency()))
	print("Row {}".format(r.randomRow(10000)))
	print("RandomPrice {0:.2f}".format(r.randomPrice()))
	print("PriceGrowth {0:.2f}".format(r.priceGrowth()))
	print("RandomPosition {}".format(r.randomPosition()))
	print("PositionGrowth {0:.2f}".format(r.positionGrowth()))