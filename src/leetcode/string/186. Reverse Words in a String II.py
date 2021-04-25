"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""


class MySolution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        l, p = 0, 0
        while p < len(s):
            while p < len(s) and s[p] != ' ':
                p += 1
            r = p - 1
            while l <= r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            p += 1
            l = p

