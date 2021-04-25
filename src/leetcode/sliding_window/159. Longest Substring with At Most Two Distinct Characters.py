"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if s == "":
            return 0

        maxlength = -1
        l, r = 0, 0
        d = {}

        while r < len(s):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1

            if len(d) > 2:
                length = r - l
                if length > maxlength:
                    maxlength = length

                while l <= r and len(d) > 2:
                    if d[s[l]] == 1:
                        del d[s[l]]
                    else:
                        d[s[l]] -= 1
                    l += 1
            r += 1

        if r - l > maxlength:
            maxlength = r - l

        return maxlength
