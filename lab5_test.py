import unittest
from lab5 import find_shortest_safe_path

class TestPathFinder(unittest.TestCase):
    def test_single_sensor(self):
        matrix1 = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        self.assertEqual(find_shortest_safe_path(matrix1), -1)

    def test_no_sensors(self):
        matrix2 = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0]
        ]
        self.assertEqual(find_shortest_safe_path(matrix2), 8)


if __name__ == '__main__':
    unittest.main()