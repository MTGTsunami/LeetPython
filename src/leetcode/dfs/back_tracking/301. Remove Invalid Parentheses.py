"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""


class Solution_Backtrack(object):  # naive backtracking
    def __init__(self):
        self.validExpr = set()
        self.minRemoved = float("inf")

    def backtrack(self, string, idx, left, right, expr, remCount):
        if idx == len(string):
            if left == right:
                if remCount <= self.minRemoved:
                    ans = "".join(expr)
                    if remCount < self.minRemoved:
                        self.validExpr = set()
                        self.minRemoved = remCount
                    self.validExpr.add(ans)
        else:
            curr = string[idx]
            if curr != "(" and curr != ")":
                expr.append(curr)
                self.backtrack(string, idx + 1, left, right, expr, remCount)
                expr.pop()
            else:
                # ignoring the current character
                self.backtrack(string, idx + 1, left, right, expr, remCount + 1)
                expr.append(curr)
                if curr == "(":
                    self.backtrack(string, idx + 1, left + 1, right, expr, remCount)
                elif right < left:
                    self.backtrack(string, idx + 1, left, right + 1, expr, remCount)
                expr.pop()

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.backtrack(s, 0, 0, 0, [], 0)
        return list(self.validExpr)


class Solution(object):  # Better backtracking

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left, right = 0, 0
        for ch in s:
            if ch == "(":
                left += 1
            elif ch == ")":
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else left
        res = set()

        def backtrack(s, idx, leftCount, rightCount, leftRem, rightRem, expr):
            if idx == len(s):
                if leftRem == 0 and rightRem == 0:
                    ans = "".join(expr)
                    res.add(ans)
            else:
                curr = s[idx]
                if (curr == "(" and leftRem > 0) or (curr == ")" and rightRem > 0):
                    backtrack(s, idx + 1, leftCount, rightCount, leftRem - (curr == "("), rightRem - (curr == ")"),
                              expr)

                # if the curr cannnot be removed:
                expr.append(curr)

                if curr != "(" and curr != ")":
                    backtrack(s, idx + 1, leftCount, rightCount, leftRem, rightRem, expr)
                elif curr == "(":
                    backtrack(s, idx + 1, leftCount + 1, rightCount, leftRem, rightRem, expr)
                elif leftCount > rightCount:
                    backtrack(s, idx + 1, leftCount, rightCount + 1, leftRem, rightRem, expr)

                expr.pop()

        backtrack(s, 0, 0, 0, left, right, [])
        return list(res)
