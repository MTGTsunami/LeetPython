"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """

            if s == "":
                return 0

            maxLength = 1
            l, r = 0, 0
            str = ""
            while r < len(s):
                if s[r] not in str:
                    str += s[r]
                else:
                    length = r - l
                    if length > maxLength:
                        maxLength = length
                    str += s[r]

                    while l <= r and s[l] != s[r]:
                        str = str.replace(str[0], "", 1)
                        l += 1
                    l += 1
                    str = str.replace(str[0], "", 1)
                r += 1

            if len(str) > maxLength:
                maxLength = len(str)

            return maxLength


