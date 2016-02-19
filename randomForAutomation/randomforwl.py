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

	def randomExchangeForRun(self):
		result = random.randint(0,4)
		if result == 0:
			return 'No'
		else:
			return 'Yes'

	def randomWLSyncType(self):
		choices = ["server", "device", "merge"]
		result = random.choice(choices)
		return result

	def randomCurrencyAndExchange(self):
		choices = [["Brazilian Real", "BZ"], ["Euro", "LN"], ["Israeli Shekel", "US"], ["Japanese Yen", "JP"], ["Malaysian Ringgit", "MK"], ["Singapore Dollar", "US"], ["South Korean Won", "US"], ["Turkish Lira", "GR"], ["US Dollar", "US"]] 
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

	def randomPosition(self, resultLimit=10000000000):
		result = random.randint(1,resultLimit)	
		return result

if __name__ == "__main__":
	r = RandomForWL()
	print("Lots {}".format(r.randomLots()))
	print("Login {}".format(r.randomLogin()))
	print("SyncType {}".format(r.randomWLSyncType()))
	print("Currency {}".format(r.randomCurrency()[0]))
	print("Row {}".format(r.randomRow(10000)))
	print("RandomPrice {0:.2f}".format(r.randomPrice()))
	print("PriceGrowth {0:.2f}".format(r.priceGrowth()))
	print("RandomPosition {}".format(r.randomPosition()))
	print("PositionGrowth {0:.2f}".format(r.positionGrowth()))