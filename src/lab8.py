import csv
from collections import deque

class CableNetwork:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        self.parent[root_b] = root_a
        return True

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i][0] < arr[left][0]:
        largest = left

    if right < n and arr[largest][0] < arr[right][0]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(edges):
    n = len(edges)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(edges, n, i)
    
    for i in range(n - 1, 0, -1):
        edges[i], edges[0] = edges[0], edges[i]
        heapify(edges, i, 0)
    
    return edges

def read_full_graph(filename):
    edges = []
    vertices = set()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            a, b, dist = row[0].strip(), row[1].strip(), int(row[2])
            edges.append((dist, a, b))
            vertices.update([a, b])
    return edges, vertices

def minimum_spanning_tree(edges, vertices):
    network = CableNetwork(vertices)
    sorted_edges = heap_sort(edges.copy())
    mst_edges = []
    total_length = 0
    edge_count = 0

    for dist, a, b in sorted_edges:
        if network.union(a, b):
            mst_edges.append((dist, a, b))
            total_length += dist
            edge_count += 1

    if edge_count == len(vertices) - 1:
        return total_length, mst_edges
    else:
        return -1, []

def build_adjacency_list(edges):
    adj = {}
    for _, a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    return adj

def print_tree(adj, node, parent=None, prefix="", is_last=True):
    connector = "\\-- " if is_last else "/-- "
    print(prefix + connector + str(node))

    children = [child for child in adj.get(node, []) if child != parent]
    for i, child in enumerate(children):
        last = i == (len(children) - 1)
        new_prefix = prefix + ("    " if is_last else "|   ")
        print_tree(adj, child, node, new_prefix, last)

def print_edges(title, edges):
    print(f"\n{title}:")
    for dist, a, b in edges:
        print(f"{a} -- {b} ({dist})")

if __name__ == "__main__":
    file = "communication_wells.csv"
    all_edges, all_vertices = read_full_graph(file)
    print_edges("Повний граф", all_edges)

    length, mst = minimum_spanning_tree(all_edges, all_vertices)

    if length != -1:
        adj = build_adjacency_list(mst)
        root = next(iter(adj))
        print("\nMST:")
        print_tree(adj, root)
        print(f"\nСумарна довжина кабелю: {length}")
    else:
        print("\nНеможливо побудувати мінімальне кістякове дерево.")