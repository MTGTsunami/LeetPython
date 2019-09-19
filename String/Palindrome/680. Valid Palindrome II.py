"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                tmp1 = s[:l] + s[l + 1:]
                tmp2 = s[:r] + s[r + 1:]
                return tmp1 == tmp1[::-1] or tmp2 == tmp2y[::-1]
        return True


class MySolution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isPalindrome(st):
            if not st:
                return True
            l = (len(st) - 1) // 2
            r = l if len(st) % 2 == 1 else l + 1
            while l >= 0 and r < len(st):
                if st[l] != st[r]:
                    return False
                l -= 1
                r += 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s[:l] + s[l + 1:]) or isPalindrome(s[:r] + s[r + 1:])
        return True










