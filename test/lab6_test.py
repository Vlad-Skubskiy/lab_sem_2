import unittest
import os
from lab6 import find_max_pyramid_path

class TestTriangleMaxPath(unittest.TestCase):
    def setUp(self):
        with open("test1_input.txt", "w") as f:
            f.write("3\n1\n2 3\n4 5 6")
        
        with open("test2_input.txt", "w") as f:
            f.write("4\n-1\n2 3\n1 -1 2\n4 5 6 7")
        
        with open("test3_input.txt", "w") as f:
            f.write("1\n10")

    def tearDown(self):

        test_files = ["test1_input.txt", "test1_output.txt",
                     "test2_input.txt", "test2_output.txt",
                     "test3_input.txt", "test3_output.txt"]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)

    def test_case1(self):
        find_max_pyramid_path("test1_input.txt", "test1_output.txt")
        
        with open("test1_output.txt", "r") as f:
            lines = f.readlines()
            self.assertEqual(lines[0].strip(), "10")
            self.assertEqual(lines[1].strip(), "1 -> 3 -> 6")

    def test_case2(self):
        find_max_pyramid_path("test2_input.txt", "test2_output.txt")
        
        with open("test2_output.txt", "r") as f:
            lines = f.readlines()
            self.assertEqual(lines[0].strip(), "12")
            path = list(map(int, lines[1].strip().split(" -> ")))
            self.assertEqual(len(path), 4)

    def test_case3(self):
        find_max_pyramid_path("test3_input.txt", "test3_output.txt")
        
        with open("test3_output.txt", "r") as f:
            lines = f.readlines()
            self.assertEqual(lines[0].strip(), "10")
            self.assertEqual(lines[1].strip(), "10")

if __name__ == "__main__":
    unittest.main()