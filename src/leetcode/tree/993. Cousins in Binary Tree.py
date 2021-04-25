"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

"""

from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        hx, hy = -1, -2
        queue = deque([(root, 0)])
        while queue:
            node, h = queue.popleft()
            if node.left:
                queue.append((node.left, h + 1))
            if node.right:
                queue.append((node.right, h + 1))
            if node.left and node.right:
                if (node.left.val == x and node.right.val == y) or \
                        (node.left.val == y and node.right.val == x):
                    return False

            if node.val == x:
                hx = h
            elif node.val == y:
                hy = h

            if hx == hy:
                return True
            elif hx > 0 and hy > 0 and hx != hy:
                return False


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionDFS_Parent(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        parent = {}
        depth = {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FastBFSSolution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root == None:
            return False
        # bfs starts with the root
        q = [(-1, root)]  # (parent, currentNode)
        while len(q) > 0:
            n = len(q)
            hs = {}
            # only iterate the nodes on the same layer
            for _ in range(n):
                # dequeue
                parent, node = q.pop(0)
                hs[node.val] = parent
                # enqueue if children are non-null
                if node.left != None:
                    q.append((node.val, node.left))
                if node.right != None:
                    q.append((node.val, node.right))
            # check if cousions
            if x in hs and y in hs:
                if hs[x] != hs[y]:
                    # yeah!!! nodes are on the same layer and have diff parents
                    return True
                else:
                    # description said that there would be no duplicate values, so it means no need to explore anymore
                    return False
        return False
