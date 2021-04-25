"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""


class SolutionDP_Best(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n

        maxarea = 0

        for i in range(m):
            cur_left, cur_right = 0, n

            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j + 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j

            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea


class SolutionDP_Dumb(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxarea = 0
        row = len(matrix)
        if row == 0:
            return 0

        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    if matrix[i][j] == "0":
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j - 1] + 1
                width = dp[i][j]

                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        return maxarea
