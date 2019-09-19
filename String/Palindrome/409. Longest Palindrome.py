"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        flag = 0
        for i in collections.Counter(s).values():
            if i % 2 == 0:
                res += i
            elif i % 2 != 0 and i > 1:
                flag = 1
                res += i - 1
            else:
                flag = 1
        if flag == 1:
            return res + 1
        else:
            return res
