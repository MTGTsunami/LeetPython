"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class MySolution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = deque([(root, 0)])
        res, prev = [], (None, 0)
        while queue:
            node, val = queue.popleft()
            if prev[1] != val:
                res.append(prev[0].val)
            if node.left:
                queue.append((node.left, val + 1))
            if node.right:
                queue.append((node.right, val + 1))
            prev = (node, val)
        res.append(node.val)
        return res
