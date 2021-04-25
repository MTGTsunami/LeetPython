"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class SolutionManacher(object):  # O(n) time, O(n) space
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # make s a string with odd length
        s = '#' + '#'.join(s) + '#'

        p = [0] * len(s)
        maxRight = 0
        pos = 0
        maxLen = 0
        maxString = ""
        for i in range(len(s)):
            if i < maxRight:
                p[i] = min(p[2 * pos - i], maxRight - i)
            else:
                p[i] = 1
            # try to expand from center, be careful for the boundary conditions
            while i - p[i] >= 0 and i + p[i] < len(s) and s[i - p[i]] == s[i + p[i]]:
                p[i] += 1
            # Update maxRight,pos
            if p[i] + i - 1 > maxRight:
                maxRight = p[i] + i - 1
                pos = i
            if p[i] - 1 > maxLen:
                maxLen = p[i] - 1
                maxString = s[i - maxLen:i + maxLen].replace("#", "")
        return maxString


class SolutionMyDP:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        else:

            lp = [[] for i in range(n)]
            for i in range(n):  # Initialize array "lp"
                for j in range(n - 1, -1, -1):
                    lp[i].append(0)

            lp[n - 1][n - 1] = 1  # Giving boundary conditions
            for i in range(n - 1):
                lp[i][i] = 1
                if s[i] == s[i + 1]:
                    lp[i][i + 1] = 1

            for j in range(2, n):  # Recurrence(traverse the triangle array in the sideling way)
                for i in range(n - j):
                    if s[i] == s[i + j]:
                        lp[i][i + j] = lp[i + 1][i + j - 1]
                    else:
                        lp[i][i + j] = 0

            longest = 0
            left = 0
            right = 0
            for i in range(n):
                for j in range(i, n):
                    if lp[i][j] == 1:
                        if j - i + 1 > longest:
                            longest = j - i + 1
                            left = i
                            right = j

            return s[left:right + 1]



class SolutionDP:  # modified solution
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""
        else:

            lp = [[0] * n for _ in range(n)]  # Initialize array "lp"
            """lp = [[] for i in range(n)]
            for i in range(n): 
                for j in range(n - 1, -1, -1):
                    lp[i].append(0)
            """

            longest = 1
            left = 0
            right = 0

            lp[n - 1][n - 1] = 1  # Giving boundary conditions
            for i in range(n - 1):
                lp[i][i] = 1
                if s[i] == s[i + 1]:
                    lp[i][i + 1] = 1
                    longest = 2
                    left = i
                    right = i + 1

            for j in range(2, n):  # Recurrence(traverse the triangle array in the sideling way)
                for i in range(n - j):
                    if s[i] == s[i + j]:
                        lp[i][i + j] = lp[i + 1][i + j - 1]
                        if lp[i][i + j] == 1:
                            if j + 1 > longest:
                                longest = j + 1
                                left = i
                                right = i + j
                    else:
                        lp[i][i + j] = 0

            return s[left:right + 1]
