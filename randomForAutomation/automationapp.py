from randomforwl import * 
from queue import *

def runApp():
	selection = ""
	r = RandomForWL()
	q = Queue()
	print("Select from the following:")
	print("  1: Print all random options.")
	print("  2: Print only random spreadsheet row.")
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
			print("SpreadsheetRow {}".format(r.randomSpreadsheetRow(2820)))
			print("RandomPrice {0:.2f}".format(r.randomPrice()))
			print("PriceGrowth {0:.2f}".format(r.priceGrowth()))
			print("RandomPosition {}".format(r.randomPosition()))
			print("PositionGrowth {0:.2f}".format(r.positionGrowth()))
		elif selection == "2":
			count = 0
			while count < 30:
				print(" ")
				count += 1
			print("SpreadsheetRow {}".format(r.randomSpreadsheetRow(2820)))
		elif selection == "3":
			ticker = raw_input("Enter ticker: ")
			q.enqueue(ticker)
		elif selection == "4":
			count = 0
			while count < 30:
				print(" ")
				count += 1
			print(q.dequeue())
		elif selection == "X":
			print("Exiting")			
		

if __name__=="__main__":
	runApp()
