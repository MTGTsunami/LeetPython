"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def merge_trees(self, t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    return t1


# My solution
def merge_trees_bfs(root1, root2):
    head = root2
    stack = [(root1, root2, None, None)]
    while stack:
        root1, root2, pre_node, direction = stack.pop()
        if root1 and root2:
            root2.val += root1.val
            stack.append((root1.right, root2.right, root2, "right"))
            stack.append((root1.left, root2.left, root2, "left"))
        elif root1 and not root2:
            if not pre_node:
                head = root1
            else:
                if direction == "left":
                    pre_node.left = root1
                elif direction == "right":
                    pre_node.right = root1
    return head
