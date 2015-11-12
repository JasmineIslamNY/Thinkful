from outputjson import OutputJSON

class KeyValuePair (object):
    def __init__(self, key, value, isList, isGroup):
        self.key = key
        self.value = value
        self.isList = isList
	self.isGroup = isGroup
        self.nextPair = None

class DataObject (object):
    def __init__(self, name="item"):
        self.name = name
        self.head = None
        self.nextReturnPair = None

    def addPair (self, pair):
        if self.head == None:
	    self.head = pair
	    self.nextReturnPair = self.head
		
        else:
            pairToAddTo = self.head
            while pairToAddTo.nextPair <> None:
                pairToAddTo = pairToAddTo.nextPair  
            pairToAddTo.nextPair = pair
        
    def addKeyValue (self, key, value):
        pair = KeyValuePair(key, value, "no", "no")
        self.addPair(pair)
        
    def addKeyList (self, key, value):
        pair = KeyValuePair(key, value, "yes", "no")
        self.addPair(pair)

    def addKeyGroup (self, key, value):
        pair = KeyValuePair(key, value, "no", "yes")
        self.addPair(pair)

    def returnNextPair(self):
        returnPair = self.nextReturnPair
        self.nextReturnPair = self.nextReturnPair.nextPair
        return returnPair 
     
if __name__ == "__main__":
    test = DataObject()
    test.addKeyValue("fname", "Jasmine")
    test.addKeyValue ("lname", "Islam")
    testchild = DataObject()
    testchild.addKeyValue ("street", "63 S Terrace Place")  
    testchild.addKeyValue ("city", "Valley Stream")   
    test.addKeyList("address", testchild)
    testchild2 = DataObject("phone_numbers")
    testchild2.addKeyValue ("home", "(516) 837-0641")  
    testchild2.addKeyValue ("mobile", "(347) 423-7387")   
    test.addKeyGroup("phones", testchild2)

    text = OutputJSON(test)
    print(text.json)


    """
    while test.nextReturnPair <> None:
        pair = test.returnNextPair()
	if pair.isList == "no" and pair.isGroup == "no":
		print ("{} : {}".format(pair.key, pair.value))
        elif pair.isList == "yes":
		print(pair.key)
		pairChild = pair.value
		while pairChild.nextReturnPair <> None:
        		grChild = pairChild.returnNextPair()
			if grChild.isList == "no" and grChild.isGroup == "no":
				print ("{} : {}".format(grChild.key, grChild.value))
	elif pair.isGroup == "yes":
		print(pair.key)
		pairChild = pair.value
		while pairChild.nextReturnPair <> None:
        		grChild = pairChild.returnNextPair()
			if grChild.isList == "no" and grChild.isGroup == "no":
				print ("{} : {}".format(grChild.key, grChild.value))
    """
       