"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class MySolution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        return haystack.find(needle)


class MySolution_2Ptr(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        n = len(haystack)
        m = len(needle)

        ptrh = 0
        while ptrh <= n - m:
            ptrn = 0
            temp = ptrh
            while ptrn < m and haystack[temp] == needle[ptrn]:
                ptrn += 1
                temp += 1
            if ptrn == m:
                return ptrh
            ptrh += 1

        return -1