"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [[] for _ in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(i + 1):
                dp[i].append(1)

        if rowIndex > 1:
            for i in range(2, rowIndex + 1):
                for j in range(1, i):
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[-1]