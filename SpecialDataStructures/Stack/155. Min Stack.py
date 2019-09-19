"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

# append(a, b) in stack, a as the input x, b as the minimum val's index currently in the stack
class MyMinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []

    def push(self, x: int) -> None:
        if not self.minstack:
            self.minstack.append((x, 0))
        else:
            if x < self.minstack[self.minstack[-1][1]][0]:
                self.minstack.append((x, len(self.minstack)))
            else:
                self.minstack.append((x, self.minstack[-1][1]))

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1][0]

    def getMin(self) -> int:
        return self.minstack[self.minstack[-1][1]][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()