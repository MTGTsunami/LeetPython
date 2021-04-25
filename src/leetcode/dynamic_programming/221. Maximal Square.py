"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class MySolution(object):  # O(N^2*M)
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    matrix[i][j] = int(matrix[i][j])
                else:
                    matrix[i][j] = int(matrix[i][j]) + matrix[i - 1][j] if \
                        matrix[i][j] != '0' else 0

        maxsquare = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    k, outOfRange = j, False
                    while k < j + matrix[i][j]:
                        if k >= len(matrix[0]):
                            outOfRange = True
                            break
                        elif matrix[i][k] < matrix[i][j]:
                            matrix[i][j] = matrix[i][k]
                        k += 1
                    if not outOfRange:
                        maxsquare = max(maxsquare, matrix[i][j] ** 2)
                    else:
                        maxsquare = max(maxsquare, (len(matrix[0]) - j) ** 2)
        return maxsquare


"""
dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.
"""


class Solution(object):  # o(MN)
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        maxsquare = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxsquare = max(maxsquare, dp[i][j] ** 2)
        return maxsquare


class BetterDP_Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        maxsquare = 0
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxsquare = max(maxsquare, dp[i][j] ** 2)
        return maxsquare