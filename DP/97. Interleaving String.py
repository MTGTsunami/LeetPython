"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""


class MySolution:  # dp time: O(mn), space: O(mn)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        n, m = len(s1), len(s2)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = True if dp[i - 1][0] and s1[i - 1] == s3[i - 1] else False
        for j in range(1, m + 1):
            dp[0][j] = True if dp[0][j - 1] and s2[j - 1] == s3[j - 1] else False

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[n][m]


class Solution:  # O(m) space dp
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1]

