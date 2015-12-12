class binaryToDecimal(object):
    def __init__(self):
        self.lastDecimal = 0 

    def convert(self, bin):
        self.lastDecimal = 0 
        string = str(bin)                
        length = len(string) - 1
      
        i = 0
        while length >= 0:
                self.lastDecimal = self.lastDecimal + (int(string[length]) * (2 ** i))
                i += 1
                length -= 1
                
        return self.lastDecimal
            
if __name__ == "__main__":
    test = binaryToDecimal()
    print("100 should be 4")
    print(test.convert("100")) 
    print("10011100 should be 156")
    print(test.convert(10011100)) 
    print("1010100010010110100 should be 345268")
    print(test.convert(1010100010010110100)) 
    print("1101 should be 13")
    print(test.convert(1101))     