"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.


Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# My solution1: Inorder Traversal
def range_sum_bst(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """
    stack = []
    total = 0
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if L <= root.val <= R:
            total += root.val
        root = root.right
    return total


# My solution 2: DFS
def range_sum_bst2(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """
    if not root:
        return 0

    return dfs(root, 0, L, R)


def dfs(node, total, L, R):
    if not node:
        return 0

    if node.val < L:
        total += dfs(node.right, total, L, R)
    elif node.val > R:
        total += dfs(node.left, total, L, R)
    else:
        total += (node.val + dfs(node.left, total, L, R) + dfs(node.right, total, L, R))
    return total
