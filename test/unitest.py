import unittest
from src.lab1 import is_monotone1
class MonotoneArray(unittest.TestCase):
    
    def test_increasing(self):
        self.assertTrue(is_monotone1([1, 2, 3, 4, 5]))
        
unittest.main()
