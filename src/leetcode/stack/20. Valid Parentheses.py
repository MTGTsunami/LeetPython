"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = Stack()
        balance = True
        i = 0

        while i < len(s) and balance:
            if s[i] in "([{":
                p.push(s[i])
            else:
                if p.isEmpty():
                    balance = False
                else:
                    left = p.pop()
                    if left == "(":
                        if s[i] in "]}":
                            balance = False
                    elif left == "[":
                        if s[i] in ")}":
                            balance = False
                    else:
                        if s[i] in ")]":
                            balance = False
            i += 1

        if p.isEmpty() and balance:
            return True
        else:
            return False
