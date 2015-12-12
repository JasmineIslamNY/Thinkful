class decimalToBinary(object):
    def __init__(self):
        self.lastBinary = "" 

    def convert(self, dec, size):
        self.lastBinary = ""        
        while dec!= 0:
            self.lastBinary = str(dec % 2) + self.lastBinary
            dec = int(dec/2)
            
        while len(self.lastBinary) < size:
            self.lastBinary = "0" + self.lastBinary
        return self.lastBinary
            
if __name__ == "__main__":
    test = decimalToBinary()
    print("4 should be 100 (5)")
    print(test.convert(4, 5)) 
    print("156 should be 10011100")
    print(test.convert(156, 6)) 
    print("345268 should be 1010100010010110100")
    print(test.convert(345268, 6)) 
    print("13 should be 1101 (6)")
    print(test.convert(13, 6))     
