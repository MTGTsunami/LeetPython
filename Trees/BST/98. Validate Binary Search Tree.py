"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def findMin(root):  # The minimum value of a tree without the node's value
            minval = 0
            if root.left is not None and root.right is not None:
                minleft = findMin(root.left)
                minright = findMin(root.right)
                minval = min(minleft, minright)
            elif root.left is not None and root.right is None:
                minval = findMin(root.left)
            elif root.left is None and root.right is not None:
                minval = findMin(root.right)
            else:
                minval = root.val
            return minval

        def findMax(root):  # The maximum value of a tree without the node's value
            maxval = 0
            if root.left is not None and root.right is not None:
                maxleft = findMax(root.left)
                maxright = findMax(root.right)
                maxval = max(maxleft, maxright)
            elif root.left is not None and root.right is None:
                maxval = findMax(root.left)
            elif root.left is None and root.right is not None:
                maxval = findMax(root.right)
            else:
                maxval = root.val
            return maxval

        BST = True
        if root is None or (root.left is None and root.right is None):
            return BST

        if root.left is not None:
            leftBST = self.isValidBST(root.left)
            maxval = findMax(root.left)
            if not leftBST or maxval >= root.val or root.left.val >= root.val:
                BST = False

        if root.right is not None:
            rightBST = self.isValidBST(root.right)
            minval = findMin(root.right)
            if not rightBST or minval <= root.val or root.right.val <= root.val:
                BST = False

        return BST


class Solution_Recurrsive:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def isBSTHelper(node, lower_limit, upper_limit):
            if lower_limit is not None and node.val <= lower_limit:
                return False
            if upper_limit is not None and upper_limit <= node.val:
                return False

            left = isBSTHelper(node.left, lower_limit, node.val) if node.left else True
            if left:
                right = isBSTHelper(node.right, node.val, upper_limit) if node.right else True
                return right
            else:
                return False

        return isBSTHelper(root, None, None)


class Solution_Iteration:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, None, None), ]
        while stack:
            root, lower_limit, upper_limit = stack.pop()
            if root.right:
                if root.right.val > root.val:
                    if upper_limit and root.right.val >= upper_limit:
                        return False
                    stack.append((root.right, root.val, upper_limit))
                else:
                    return False
            if root.left:
                if root.left.val < root.val:
                    if lower_limit and root.left.val <= lower_limit:
                        return False
                    stack.append((root.left, lower_limit, root.val))
                else:
                    return False
        return True


class Solution_InoderTraversal:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True