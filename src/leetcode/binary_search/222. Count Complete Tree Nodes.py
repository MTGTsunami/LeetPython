"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class NaiveSolution:
    def countNodes(self, root: TreeNode) -> int:
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_BinarySearch:
    def depth(self, node: TreeNode) -> int:
        """
        return the depth of the complete binary tree in O(h) time
        """
        h = 0
        while node.left:
            h += 1
            node = node.left
        return h

    def exists(self, idx: int, h: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**h - 1 (left -> right).
        Return True if last level node idx exists.
        Binary search with O(h) complexity.
        """
        left, right = 0, 2 ** h - 1
        for _ in range(h):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        h = self.depth(root)
        if h == 0:
            return 1
        left, right = 0, 2 ** h - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, h, root):
                left = pivot + 1
            else:
                right = pivot - 1

        return (2 ** h - 1) + left

