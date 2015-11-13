from outputjson import OutputJSON

class KeyValuePair (object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.kind = "single"
        self.nextPair = None

class DataObject (object):
    def __init__(self, name="item", kind="default"):
        self.name = name
        self.kind = kind
        self.nextPair = None
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
        pair = KeyValuePair(key, value)
        self.addPair(pair)
    """   
    def addKeyList (self, key, value):
        pair = KeyValuePair(key, value, "yes", "no")
        self.addPair(pair)

    def addKeyGroup (self, key, value):
        pair = KeyValuePair(key, value, "no", "yes")
        self.addPair(pair)
    """
    
    def returnNextPair(self):
        returnPair = self.nextReturnPair
        self.nextReturnPair = self.nextReturnPair.nextPair
        return returnPair 
     
if __name__ == "__main__":
    test = DataObject()
    test.addKeyValue("fname", "Jasmine")
    test.addKeyValue ("lname", "Islam")
    testchild1 = DataObject("address", "list")
    grandchild1 = DataObject("addressitem", "group")
    grandchild1.addKeyValue ("street", "63 S Terrace Place")  
    grandchild1.addKeyValue ("city", "Valley Stream")   
    grandchild2 = DataObject("addressitem", "group")
    grandchild2.addKeyValue ("street", "731 Lexington Ave")  
    grandchild2.addKeyValue ("city", "New York")
    testchild1.addPair(grandchild1)
    testchild1.addPair(grandchild2)
    test.addPair(testchild1)
    testchild2 = DataObject("phone_numbers", "group")
    testchild2.addKeyValue ("home", "(516) 837-0641")  
    testchild2.addKeyValue ("mobile", "(347) 423-7387")   
    test.addPair(testchild2)

    
    text = OutputJSON(test)
    print(text.json)


    """    
    while test.nextReturnPair <> None:
        pair = test.returnNextPair()
	if pair.kind == "single":
		print ("{} : {}".format(pair.key, pair.value))
        elif pair.kind == "list":
		print(pair.name)
		while pair.nextReturnPair <> None:
			pairChild = pair.returnNextPair()
			print ("{} : {}".format(pairChild.key, pairChild.value))
	elif pair.kind == "group":
		print(pair.name)
		while pair.nextReturnPair <> None:
			pairChild = pair.returnNextPair()
			print ("{} : {}".format(pairChild.key, pairChild.value))
   
    """ 
