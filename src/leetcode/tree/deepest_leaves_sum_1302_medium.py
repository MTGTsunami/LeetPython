"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# My solution: BFS
def deepest_leave_sum(root) -> int:
    from collections import deque
    queue = deque([(root, 0)])
    pre_level, total = 0, 0
    while queue:
        root, level = queue.popleft()
        if level != pre_level:
            total = 0
            pre_level = level
        total += root.val
        if root.left:
            queue.append((root.left, level + 1))
        if root.right:
            queue.append((root.right, level + 1))
    return total