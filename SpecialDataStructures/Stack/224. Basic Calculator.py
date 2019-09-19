"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class MySolution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        isPlus = False
        isMinus = False
        isNum = False
        count = 0

        for i, char in enumerate(s):
            if char != " ":
                if not stack:
                    if char.isdigit():
                        stack.append(int(char))
                        isNum = True
                    else:
                        stack.append(char)
                        stack.append(0)
                    continue

                if char == '(':
                    stack.append(char)
                    stack.append(0)
                elif char == ')':
                    temp1 = stack.pop()
                    stack.pop()
                    if not stack:
                        stack.append(temp1)
                    else:
                        notation = stack.pop()
                        if notation == '+':
                            stack[-1] += temp1
                        else:
                            stack[-1] -= temp1
                elif char == '+' or char == '-':
                    isNum = False
                    if s[i + 1] == '(':
                        stack.append(char)
                    else:
                        if char == '+':
                            isPlus = True
                        else:
                            isMinus = True
                else:
                    if isPlus or isMinus:
                        count = 10 * count + int(char)
                        if i + 1 >= len(s) or not s[i + 1].isdigit():
                            if isPlus:
                                stack[-1] += count
                                isPlus = False
                            else:
                                stack[-1] -= count
                                isMinus = False
                            count = 0
                    elif isNum:
                        stack[-1] = stack[-1] * 10 + int(char)
                    else:
                        stack[-1] += int(char)
                        isNum = True
        return stack[0]



