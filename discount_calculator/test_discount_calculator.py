import unittest

from discount_calculator import discount_calculator

class DiscountCalculatorTests(unittest.TestCase):
    def testNormal(self):
        discounted_price = discount_calculator(200, 10, 25 )

        # Check that the right values are returned
        self.assertEqual(discounted_price, 155)
        
    def testNormal2(self):
        discounted_price = discount_calculator(200, .10, 25.5 )
        self.assertEqual(discounted_price, 154.5)        

    def testZeroDiscount(self):
        discounted_price = discount_calculator(200, 0, 0 )
        self.assertEqual(discounted_price, 200)
        
    def testNegativeResult(self):
        discounted_price = discount_calculator(200, 90, 100 )
        self.assertEqual(discounted_price, 0)
 
    def testNegativeResult2(self):
        discounted_price = discount_calculator(200, 900, 100 )
        self.assertEqual(discounted_price, 0)        
   
    def testNegativeResult3(self):
        discounted_price = discount_calculator(200, 90, 1000 )
        self.assertEqual(discounted_price, 0)        
        
    def testTinyResult(self):
        discounted_price = discount_calculator(100, 99, .99 )
        self.assertEqual(discounted_price, 0.01)       
        
    def testTinyDiscount(self):
        discounted_price = discount_calculator(200, 1, .01 )
        self.assertEqual(discounted_price, 197.99)         
        
    def testNegativePrice(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator(-200, 10, 25 )
            
    def testNegativeRelative(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator(200, -10, 25 )
            
    def testNegativeAbsolute(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator(200, 10, -25 )
            
    def testNegativeAll(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator(-200, -90, -100 )
                            
    def testTextPrice(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator('a', 10, 25 ) 
            
    def testTextRelative(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator(20, 'a', 25 ) 
            
    def testTextAbsolute(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator(20, 10, 'a' )
            
    def testTextAll(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator('a', 'b', 'c' )   
            
    def testList(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator([1, 2], 10, 25 )                                                                  

    def testDict(self):
        with self.assertRaises(ValueError):
            discounted_price = discount_calculator({'a': 200}, 10, 25 ) 

if __name__ == "__main__":
    unittest.main()

