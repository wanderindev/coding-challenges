class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invert_tree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        left = root.left
        root.left = root.right
        root.right = left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root


# Test cases
sol = Solution()

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

inv_tree = sol.invert_tree(tree)

assert inv_tree.val == 4
assert inv_tree.left.val == 7
assert inv_tree.right.val == 2
assert inv_tree.left.left.val == 9
assert inv_tree.left.right.val == 6
assert inv_tree.right.left.val == 3
assert inv_tree.right.right.val == 1
