"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.
"""


class SolutionMyDP(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = n
        if n == 0:
            return count

        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n - 1):
            dp[i][i] = True
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1
        dp[n - 1][n - 1] = True

        for i in range(n - 3, -1, -1):
            for j in range(n - 1, i + 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j]:
                        count += 1
        return count


class SolutionExpandFromCenter(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for center in range(2*n - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans