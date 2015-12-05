class JASMurmur32(object):
	def __init__(self, seed=55):
		self.seed = seed
		self.c1 = 148957879
		self.c2 = 489205790
		self.r1 = 15
		self.r2 = 13
		self.m = 5
		self.n = 389402
		
	def createHash(self, key):
		hash = self.seed
		chunks = len(str(key)) / 4
		for i in range(0, chunks):
			k = key[i]
			k = ord(k)
			k *= self.c1
			k *= self.c2
			
			hash ^= k
			hash = hash * self.m + self.n

		tempHash = str(hash)
		hash = 0
		for i in range(0, len(tempHash)):
			hash += int(tempHash[i])	
	
		divider = (10 ** (len(str(hash)))) * 1.0		
		hash = hash/divider		#turn hash into the format 0.hash)

		
		hash *= 0.1			#turn hash into the format 0.0hash)
		tempHash = tempHash[1]
		tempHash = float(tempHash) * 0.1
		hash += tempHash
			

		#print(hash)
		hash = int(32 * hash)	

		return hash

if __name__ == "__main__":
	test = JASMurmur32()
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("Today is Saturday")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("Today is Saturday")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("Today is Saturday")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("Today is Saturday")
	print(returnedHash)

	print("-------------------")
	print(" ")
	test = JASMurmur32(3463)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("Today is Saturday")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("Today is Saturday")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("Today is Saturday")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("Today is Saturday")
	print(returnedHash)
			
	print("-------------------")
	print(" ")
	test = JASMurmur32(9)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("priority mail")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("bbbbbbbb")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("zzzzzzzz")
	print(returnedHash)
	returnedHash = test.createHash("Mary had a little lamb")
	print(returnedHash)
	returnedHash = test.createHash("ZZZZZZZZ")
	print(returnedHash)
			