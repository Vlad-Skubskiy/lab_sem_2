import unittest
from io import StringIO
import sys
from lab9 import electrics

class TestElectrics(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_normal_case(self):
        sys.stdin = StringIO("2\n3 3 3")
        electrics()
        self.assertEqual(self.held_output.getvalue().strip(), "5.66")

    def test_single_point(self):
        sys.stdin = StringIO("5\n10")
        electrics()
        self.assertEqual(self.held_output.getvalue().strip(), "0.0")

if __name__ == "__main__":
    unittest.main()