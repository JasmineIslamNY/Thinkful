from randomforwl import * 
from queue import *
from tickers import *

def runApp():
	selection = ""
	r = RandomForWL()
	q = Queue()
	t = Tickers()
	print("Select from the following:")
	print("  1: Print all random options.")
	print("  2: Print a random position.")
	print("  3: Add ticker to Queue.")
	print("  4: Retrieve ticker from Queue.")
	print("  X: Exit")
	while selection != "X":
		selection = raw_input("Enter your selection: ")
		if selection == "1":
			print("Lots {}".format(r.randomLots()))
			print("Login {}".format(r.randomLogin()))
			print("SyncType {}".format(r.randomWLSyncType()))
			print("Currency {}".format(r.randomCurrency()))
			tick = r.randomRow(2820)
			limit = r.randomResultLimit(5)
			print("RandomTicker {}".format(t.returnTicker(tick)[0]))
			print("TickerCountry {}".format(t.returnTicker(tick)[1]))
			print("RandomPrice {0:.2f}".format(r.randomPrice(limit)))
			print("PriceGrowth {0:.2f}".format(r.priceGrowth()))
			print("RandomPosition {}".format(r.randomPosition(limit)))
			print("PositionGrowth {0:.2f}".format(r.positionGrowth()))
		elif selection == "2":
			count = 0
			while count < 30:
				print(" ")
				count += 1
			tick = r.randomRow(2820)
			limit = r.randomResultLimit(5)
			print("RandomTicker {}".format(t.returnTicker(tick)[0]))
			print("TickerCountry {}".format(t.returnTicker(tick)[1]))
			print("RandomPrice {0:.2f}".format(r.randomPrice(limit)))
			print("RandomPosition {}".format(r.randomPosition(limit)))
		elif selection == "3":
			tick = raw_input("Enter ticker: ")
			country = raw_input("Enter country: ")
			ticker = [tick, country]
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
		elif selection == "X" or selection == "x":
			if selection == "x":
				selection = "X"
			print("Exiting")			
		

if __name__=="__main__":
	runApp()
