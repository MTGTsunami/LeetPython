"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""

import collections


class MySolution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k == 0:
            return 0

        maxLength = 0
        mainPtr, fastPtr = 0, 0
        d = collections.defaultdict(int)
        while fastPtr < len(s):
            if len(d) < k or s[fastPtr] in d:
                d[s[fastPtr]] += 1
                fastPtr += 1
            else:
                maxLength = max(maxLength, fastPtr - mainPtr)
                d[s[mainPtr]] -= 1
                if d[s[mainPtr]] == 0:
                    del d[s[mainPtr]]
                mainPtr += 1
        maxLength = max(maxLength, fastPtr - mainPtr)
        return maxLength
