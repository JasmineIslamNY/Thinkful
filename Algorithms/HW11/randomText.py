import time
import random

class randomText(object):
	def __init__(self):
		self.lastText = ""

	def createText(self):
		count = 0
		while count < 6:
			now = time.time()
			now *= random.random()
			now = int(now)
			print(now)
			time.sleep(1)
			count += 1

if __name__ == "__main__":
	test = randomText()
	test.createText()
	