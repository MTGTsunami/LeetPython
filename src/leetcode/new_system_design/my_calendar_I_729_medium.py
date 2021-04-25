"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
Your class will have the method, book(int start, int end).
Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
For each call to the method MyCalendar.book,
return true if the event can be added to the calendar successfully without causing a double booking.
Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""


# naive solution
class MyCalendar:

    def __init__(self):
        self.store = []

    def book(self, start: int, end: int) -> bool:
        for event in self.store:
            if self.is_overlap(event[0], start, event[1], end):
                return False
        self.store.append((start, end))
        return True

    def is_overlap(self, s1, s2, e1, e2):
        return max(s1, s2) < min(e1, e2)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# Binary search tree
class Node:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, node, root=None):
        """
        :root type[Node] means start from which tree node to insert
        None means start from the root of the tree (self.root)
        """
        if not root:
            if not self.root:
                self.root = node
                return True
            else:
                root = self.root

        if node.end <= root.start:
            if not root.left:
                root.left = node
            else:
                return self.insert(node, root.left)
        elif node.start >= root.end:
            if not root.right:
                root.right = node
            else:
                return self.insert(node, root.right)
        else:
            return False
        return True


class MyCalendar2:

    def __init__(self):
        self.tree = Tree()

    def book(self, start: int, end: int) -> bool:
        return self.tree.insert(Node(start, end))

