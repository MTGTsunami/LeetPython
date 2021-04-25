"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        while root and (root.val < L or root.val > R):
            if root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left

        rl, rr = root, root
        while rl:
            if rl.val == L:
                rl.left = None
                rl = rl.left
            elif rl.val > L:
                temp = rl
                rl = rl.left
            else:
                rl = rl.right
                temp.left = rl

        while rr:
            if rr.val == R:
                rr.right = None
                rr = rr.right
            elif rr.val < R:
                temp = rr
                rr = rr.right
            else:
                rr = rr.left
                temp.right = rr
        return root
