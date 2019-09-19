"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_Iterative(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


class Solution_Recursive:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inOrder(root, l):
            if root is not None:
                inOrder(root.left, l)
                l.append(root.val)
                inOrder(root.right, l)
            return l

        l = []
        inOrder(root, l)
        return l