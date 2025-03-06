import unittest
from lab1 import is_monotone1
class MonotoneArray(unittest.TestCase):
    
    def test_increasing(self):
        self.assertTrue(is_monotone1([1, 2, 3, 4, 5]))
        
    # def test_decreasing(self):
    #     self.assertTrue(is_monotone2([5, 4, 3, 2, 1]))
        
unittest.main()
