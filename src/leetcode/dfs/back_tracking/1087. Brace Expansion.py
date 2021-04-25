"""
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.



Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]


Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.
"""


class MySolution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        group, part = [], []
        for ch in S:
            if ch == "}":
                part.sort()
                group.append(part)
                part = []
            elif ch == "{" and len(part) != 0:
                s = "".join(part)
                group.append([s])
                part = []
            elif ch.isalpha():
                part.append(ch)
        if len(part) != 0:
            s = "".join(part)
            group.append([s])

        def backtrack(idx, expr):
            if idx == len(group):
                s = "".join(expr)
                res.append(s)
            else:
                for c in group[idx]:
                    expr.append(c)
                    backtrack(idx + 1, expr)
                    expr.pop()

        res = []
        backtrack(0, [])
        return res

