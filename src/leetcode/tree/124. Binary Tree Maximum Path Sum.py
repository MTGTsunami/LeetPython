"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxSum(root):
            nonlocal maxZigzag
            nonlocal maxSingle

            if not root:
                return 0

            maxSumLeft = maxSum(root.left)
            maxSumRight = maxSum(root.right)
            maxSinglePath = max(max(maxSumLeft, maxSumRight) + root.val, root.val)
            zigzagPath = max(maxSumLeft + maxSumRight + root.val, root.val)
            maxSingle = max(maxSingle, maxSinglePath)
            maxZigzag = max(maxZigzag, zigzagPath)
            return maxSinglePath

        maxZigzag = -float("inf")
        maxSingle = -float("inf")
        maxSum(root)
        return int(max(maxSingle, maxZigzag))