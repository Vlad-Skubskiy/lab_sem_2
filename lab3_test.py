import unittest
from lab3 import TreeNode, is_balanced_tree

class TestBinaryTree(unittest.TestCase):

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertTrue(is_balanced_tree(root))

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)

        self.assertFalse(is_balanced_tree(root))

if __name__ == '__main__':
    unittest.main()
