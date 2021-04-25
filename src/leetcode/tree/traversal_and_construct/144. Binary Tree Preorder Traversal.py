"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_Recursive:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preOrder(root):
            if root is not None:
                l.append(root.val)
                preOrder(root.left)
                preOrder(root.right)

        l = []
        preOrder(root)
        return l


class Solution_Iterative:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root], []

        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)

        return output
