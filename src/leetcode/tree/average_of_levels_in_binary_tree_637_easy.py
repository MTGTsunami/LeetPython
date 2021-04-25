"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10-5 of the actual answer will be accepted.

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# My solution
def average_of_levels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    ans, prev_level, summ, num = [], 0, 0, 0
    queue = deque([(root, prev_level)])
    while queue:
        node, level = queue.popleft()
        if prev_level == level:
            summ += node.val
            num += 1
        else:
            ans.append(summ/num)
            num = 1
            summ = node.val
            prev_level = level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    ans.append(summ/num)
    return ans
