from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_balanced_tree(root: TreeNode) -> bool:
    if not root:
        return True

    stack = []
    node = root
    visited = None
    heights = {}

    while stack or node :
        if node:
            stack.append(node)
            node = node.left
        else:
            peek = stack[-1]
            if peek.right and (visited != peek.right):
                node = peek.right
            else:
                left_height = heights.get(peek.left, 0)
                right_height = heights.get(peek.right, 0)

                if abs(left_height - right_height) > 1:
                    return False

                heights[peek] = max(left_height, right_height) + 1
                visited = stack.pop()

    return True

def bfs_tree(root):
    if not root:
        return ["Null"]

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level.append(str(node.value))
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append("Null")

        result.append(" ".join(level))

    return result

def _print(root, filename):
    lines = bfs_tree(root)
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(6)

if is_balanced_tree(root):
    print("The tree is balanced")
else:
    print("The tree isn't balanced")
_print(root, "tree.txt")