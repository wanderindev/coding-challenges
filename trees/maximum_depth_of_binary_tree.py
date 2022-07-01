from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def max_depth_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1 + max(
            self.max_depth_recursive(root.left),
            self.max_depth_recursive(root.right),
        )

    def max_depth_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level

    def max_depth_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        stack = deque([(root, 1)])

        while stack:
            node, depth = stack.pop()

            if node:
                level = max(level, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return level


# Test cases
sol = Solution()

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

assert sol.max_depth_recursive(tree) == 3
assert sol.max_depth_bfs(tree) == 3
assert sol.max_depth_dfs(tree) == 3

tree = TreeNode(1)
tree.right = TreeNode(2)

assert sol.max_depth_recursive(tree) == 2
assert sol.max_depth_bfs(tree) == 2
assert sol.max_depth_dfs(tree) == 2
