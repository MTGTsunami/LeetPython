"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.



Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false


Notes:

Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.


Follow up:

As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""


class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.v = v
        self.row = 0
        self.col = 0
        self.flag = 0

    def next(self):
        """
        :rtype: int
        """
        self.flag += 1
        self.avoidEmptyRow()
        temp = self.v[self.row][self.col]
        if self.col + 1 == len(self.v[self.row]):
            self.row += 1
            self.avoidEmptyRow()
            self.col = 0
        else:
            self.col += 1
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.flag == 0:
            self.avoidEmptyRow()
        if self.row < len(self.v):
            return True

    def avoidEmptyRow(self):
        while self.row < len(self.v) and len(self.v[self.row]) <= 0:
            self.row += 1

        # Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()