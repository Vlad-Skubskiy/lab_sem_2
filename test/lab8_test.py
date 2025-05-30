import unittest
import csv
import os
from collections import deque

from src.lab8 import CableNetwork, heapify, heap_sort, read_full_graph, minimum_spanning_tree, build_adjacency_list

class TestCableNetwork(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_filename = "test_communication_wells.csv"
        with open(cls.test_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["A", "B", "3"])
            writer.writerow(["B", "C", "1"])
            writer.writerow(["A", "C", "2"])
            writer.writerow(["C", "D", "4"])
            writer.writerow(["D", "E", "5"])

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_filename)

    def test_cable_network_union_find(self):
        vertices = {'A', 'B', 'C'}
        network = CableNetwork(vertices)
        
        self.assertEqual(network.find('A'), 'A')
        self.assertEqual(network.find('B'), 'B')
        self.assertEqual(network.find('C'), 'C')
        
        self.assertTrue(network.union('A', 'B'))
        self.assertEqual(network.find('B'), 'A')
        
        self.assertFalse(network.union('A', 'B'))
        
        self.assertTrue(network.union('B', 'C'))
        self.assertEqual(network.find('C'), 'A')

    def test_heapify(self):
        arr = [(3, 'A', 'B'), (1, 'B', 'C'), (2, 'A', 'C')]
        n = len(arr)
        
        heapify(arr, n, 0)
        
        self.assertEqual(arr[0][0], 3)

    def test_heap_sort(self):
        edges = [(3, 'A', 'B'), (1, 'B', 'C'), (2, 'A', 'C')]
        sorted_edges = heap_sort(edges.copy())
        
        self.assertEqual(sorted_edges, [(1, 'B', 'C'), (2, 'A', 'C'), (3, 'A', 'B')])

    def test_read_full_graph(self):
        edges, vertices = read_full_graph(self.test_filename)
        
        self.assertEqual(len(edges), 5)
        self.assertEqual(len(vertices), 5)
        self.assertIn(('A', 'B', 3), [(a, b, dist) for dist, a, b in edges])
        self.assertIn('E', vertices)

    def test_minimum_spanning_tree(self):
        edges, vertices = read_full_graph(self.test_filename)
        total_length, mst = minimum_spanning_tree(edges, vertices)
        
        self.assertEqual(total_length, 1 + 2 + 4 + 5)
        self.assertEqual(len(mst), 4)


if __name__ == '__main__':
    unittest.main()