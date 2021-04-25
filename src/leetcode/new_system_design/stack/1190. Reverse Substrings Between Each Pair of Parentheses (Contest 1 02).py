"""
Given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any bracket.

"""


class MySolution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        chStack = []
        idxStack = []

        for i, ch in enumerate(s):
            chStack.append(ch)
            if ch != ")":
                if ch == "(":
                    idxStack.append(i)
            else:
                idx = idxStack.pop()
                chStack[idx:] = reversed(chStack[idx:])

        out = ""
        for ch in chStack:
            if ch != "(" and ch != ")":
                out += ch
        return out







