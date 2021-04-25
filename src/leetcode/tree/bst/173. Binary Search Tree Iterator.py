"""
Implement an iterator over a binary search tree (bst). Your iterator will be initialized with the root node of a bst.

Calling next() will return the next smallest number in the bst.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the bst when next() is called.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        self.root = self.stack.pop()
        temp = self.root
        self.root = self.root.right
        return temp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack != [] or self.root is not None

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()