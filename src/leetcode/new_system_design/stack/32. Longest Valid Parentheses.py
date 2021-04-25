"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0

        stack = []
        maxlength = -1
        for i, x in enumerate(s):
            if x == '(':
                stack.append(('(', i))
            else:
                if stack:
                    if stack[-1][0] == '(':
                        stack.pop()
                    else:
                        stack.append((')', i))
                else:
                    stack.append((')', i))

        k = 0
        stack.insert(0, (' ', -1))
        stack.append((' ', len(s)))
        while k < len(stack) - 1:
            length = stack[k + 1][1] - stack[k][1] - 1
            if length > maxlength:
                maxlength = length
            k += 1

        return maxlength