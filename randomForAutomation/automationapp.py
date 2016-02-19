from randomforwl import * 
from queue import *
from tickers import *

def runApp():
	selection = ""
	randomExchangeForRun = ""
	randomCurrencyAndExchange = ""
	r = RandomForWL()
	q = Queue()
	t = Tickers()
	print("Select from the following:")
	print("  1: Print options for test run.")
	print("  2: Print a random position. (also adds to Queue)")
	print("  3: Add ticker to Queue.")
	print("  4: Retrieve ticker from Queue.")
	print("  X: Exit")
	while selection != "X":
		selection = raw_input("Enter your selection: ")
		if selection == "1":
			#Choose the currency and exchange for this run and save for the object
			randomCurrencyAndExchange = r.randomCurrencyAndExchange()
			#Choose whether the test will be exclusive for one exchange or securities from any exchange are fine (only 1/5 will be for a single exchange)
			randomExchangeForRun = r.randomExchangeForRun()

			print("Lots {}".format(r.randomLots()))
			print("Login {}".format(r.randomLogin()))
			print("SyncType {}".format(r.randomWLSyncType()))
			print("Currency {}".format(randomCurrencyAndExchange[0]))
			print("Exchange {}".format(randomCurrencyAndExchange[1]))
			print("Random Exchange {}".format(randomExchangeForRun))

			"""
			tick = r.randomRow(2820)
			limit = r.randomResultLimit(5)
			print("RandomTicker {}".format(t.returnTicker(tick)[0]))
			print("TickerCountry {}".format(t.returnTicker(tick)[1]))
			print("RandomPrice {0:.2f}".format(r.randomPrice(limit)))
			print("PriceGrowth {0:.2f}".format(r.priceGrowth()))
			print("RandomPosition {}".format(r.randomPosition(limit)))
			print("PositionGrowth {0:.2f}".format(r.positionGrowth()))
			"""
		elif selection == "2":
			count = 0
			while count < 30:
				print(" ")
				count += 1

			#create random ticker, check if random exchange is yes/no, and depending on that check if random ticker exchange matches run's selected exchange
			x = 0
			tempTicker = ""
			while x == 0:
				tick = r.randomRow(2820)
				tempTicker = t.returnTicker(tick)
				if randomExchangeForRun == "No":
					if tempTicker[1] == randomCurrencyAndExchange[1]:
						x = 1
				else:
					x = 1

			limit = r.randomResultLimit(5)

			#assign random ticker, and price and position
			rndTicker = tempTicker[0]
			rndCountry = tempTicker[1]
			rndPrice = r.randomPrice(limit)
			rndPosition = r.randomPosition(limit)

			#save the position to the queue for retrieval later
			position = [rndTicker, rndCountry, rndPrice, rndPosition]
			q.enqueue(position)

			#print the information to the screen for Perfecto to ingest
			print("RandomTicker {}".format(rndTicker))
			print("TickerCountry {}".format(rndCountry))
			print("RandomPrice {0:.2f}".format(rndPrice))
			print("RandomPosition {}".format(rndPosition))

		elif selection == "3":
			tick = raw_input("Enter ticker: ")
			country = raw_input("Enter country: ")
			price = raw_input("Enter price: ")
			position = raw_input("Enter position: ")
			ticker = [tick, country, price, position]
			q.enqueue(ticker)

		elif selection == "4":
			count = 0
			while count < 30:
				print(" ")
				count += 1
			ticker = q.dequeue()
			if ticker == None:
				print("Something went wrong")
			else:
				print("Ticker {}".format(ticker[0]))
				print("Country {}".format(ticker[1]))
				print("Price {0:.2f}".format(ticker[2]))
				print("Position {}".format(ticker[3]))
		elif selection == "X" or selection == "x":
			if selection == "x":
				selection = "X"
			print("Exiting")			
		

if __name__=="__main__":
	runApp()
