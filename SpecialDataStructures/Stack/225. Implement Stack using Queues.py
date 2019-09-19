"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""

from collections import deque

# My solution using two queues
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue0 = deque()
        self.queue1 = deque()
        self.p = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if not self.p:
            self.queue0.append(x)
        else:
            self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.p:
            while len(self.queue0) != 1:
                self.queue1.append(self.queue0.popleft())
            self.p = 1
            return self.queue0.popleft()
        else:
            while len(self.queue1) != 1:
                self.queue0.append(self.queue1.popleft())
            self.p = 0
            return self.queue1.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.p:
            while len(self.queue0) != 1:
                self.queue1.append(self.queue0.popleft())
            return self.queue0[0]
        else:
            while len(self.queue1) != 1:
                self.queue0.append(self.queue1.popleft())
            return self.queue1[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue0) + len(self.queue1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


from collections import deque


class MyStackOneQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        i = len(self.queue)
        while i > 1:
            self.queue.append(self.queue.popleft())
            i -= 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()