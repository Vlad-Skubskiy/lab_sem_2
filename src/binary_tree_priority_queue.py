class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}({self.priority})"

class PriorityQueueTree:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if not self.root:
            self.root = new_node
        else:
            self.root = self._insert_node(self.root, new_node)

    def _insert_node(self, current, new_node):
        if not current:
            return new_node

        if new_node.priority <= current.priority:
            current.left = self._insert_node(current.left, new_node)
        else:
            current.right = self._insert_node(current.right, new_node)

        return current

    def pop(self):
        if not self.root:
            return None
        self.root, max_node = self._remove_max(self.root)
        return max_node

    def _remove_max(self, node):

        if not node.left:
            return node.right, node

        node.left, max_node = self._remove_max(node.left)
        return node, max_node

    def peek(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current

    def print_tree(self):
        def print_node(node, level=0):
            if node:
                print_node(node.right, level + 1)
                print("   " * level + str(node))
                print_node(node.left, level + 1)
        print_node(self.root)
        
pq = PriorityQueueTree()

pq.insert("A", 5)
pq.insert("B", 2)
pq.insert("C", 1)
pq.insert("D", 3)

pq.print_tree()

print("\nPeek:", pq.peek())

print("\nPop:", pq.pop())
print("\nPop:", pq.pop())
