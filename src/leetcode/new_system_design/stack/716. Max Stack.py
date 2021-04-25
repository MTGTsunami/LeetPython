"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""


class MaxStack(list):  # inheritance

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.append((x, max(x, self[-1][1] if len(self) != 0 else float("-inf"))))

    def pop(self):  # This is an override method
        """
        :rtype: int
        """
        return list.pop(self)[0]
        # return self.pop()[0] will recursively call itself.

    def top(self):
        """
        :rtype: int
        """
        return self[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        temp = []
        m = self[-1][1]
        while self[-1][0] != m:
            temp.append(self.pop())
        self.pop()
        map(self.push, reversed(temp))
        return m

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

