import time
import random

class randomText(object):
	def __init__(self):
		self.lastText = ""
		self.ascii = 91  	#ascii z is 122 and space is 32 (123-32)

	def createRandomWord(self, limit=100):
		word = ""
		now = time.time()
		now *= random.random()
		now = str(now)
		skip = int(now[0])

		stop = 0

		while stop < limit:
			stop += skip
			word = word + self.createRandomLetter()

		return word				
	
	def createRandomLetter(self):
		now = time.time()
		now *= random.random()
		now = int(now)

		tempNow = str(now)

		divider = (10 ** (len(tempNow))) * 1.0		
		now =  now/divider		#turn now into the format 0.now)

		
		now *= 0.1			#turn hash into the format 0.0now)
		tempNow = tempNow[1]
		tempNow = float(tempNow) * 0.1
		now += tempNow
			
		now = (int(self.ascii * now)) + 32 	#32 is ascii start	
		
		#print(now)
		letter = chr(now)
		time.sleep(0.25)
		return letter	





if __name__ == "__main__":
	test = randomText()
	letter = test.createRandomLetter()
	print("Random letter is {}".format(letter))

	word = test.createRandomWord()
	print("Random word is {}".format(word))	
	