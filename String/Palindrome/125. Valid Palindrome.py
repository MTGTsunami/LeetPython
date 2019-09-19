"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "")
        s = s.lower()

        n = len(s)
        l, r = (n - 1) // 2, (n - 1) // 2 + (n - 1) % 2
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        if l >= 0:
            return False
        else:
            return True

