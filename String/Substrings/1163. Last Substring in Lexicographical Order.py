"""
Given a string s, return the last substring of s in lexicographical order.



Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"


Note:

1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""

from collections import defaultdict


class MySolution:  # naive solution
    def lastSubstring(self, s: str) -> str:
        if not s:
            return ""

        subStrings = defaultdict(list)
        maxChar = ""
        for i, c in enumerate(s):
            maxChar = max(maxChar, c)
            subStrings[c].append(i)

        if len(subStrings) == 1:  # In order to handle the worst test case
            return s

        maxSub, compare = 0, 1
        while compare < len(subStrings[maxChar]):
            p1, p2 = subStrings[maxChar][maxSub], subStrings[maxChar][compare]
            while p2 < len(s):
                if s[p1] < s[p2]:
                    maxSub = compare
                    break
                elif s[p1] == s[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    break
            compare += 1
        return s[subStrings[maxChar][maxSub]:]


class Solution:  # O(n)
    def lastSubstring(self, s: str) -> str:
        i, j, offset = 0, 1, 0
        while i + offset < len(s) and j + offset < len(s):
            if s[i+offset] == s[j+offset]:
                offset += 1
            else:
                if s[i+offset] < s[j+offset]:
                    i += offset + 1
                else:
                    j += offset + 1
                if i == j:
                    i += 1
                offset = 0
        return s[min(i, j):]

