"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            val = preorder.pop(0)
            idx = inorder.index(val)
            root = TreeNode(val)
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx + 1:])
            return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_Dict:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inor_dict = {}
        for i, num in enumerate(inorder):
            inor_dict[num] = i
        pre_iter = iter(preorder)

        def helper(start, end):
            if start > end: return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            idx = inor_dict[root_val]
            root.left = helper(start, idx - 1)
            root.right = helper(idx + 1, end)
            return root

        return helper(0, len(inorder) - 1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_helper:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root

        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()
