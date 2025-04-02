class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_balanced_tree(root: TreeNode) -> int:
    def dfs(node):

        if node is None:
            return 0
        
        left_depth = dfs(node.left) 
        right_depth = dfs(node.right)
        
        if abs(left_depth - right_depth) > 1:
            return -1
        
        return max(left_depth, right_depth) + 1

    return dfs(root) != -1

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

