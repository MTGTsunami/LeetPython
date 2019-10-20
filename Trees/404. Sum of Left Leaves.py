"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root, total):
            if not root:
                return 0
            if root.left:
                if not root.left.left and not root.left.right:
                    total += root.left.val
                else:
                    total = dfs(root.left, total)
            if root.right:
                total = dfs(root.right, total)
            return total

        total = dfs(root, 0)
        return total