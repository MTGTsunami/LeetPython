"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mps = [[0 for i in range(n + 1)] for i in range(m + 1)]  # Initialize the array mps

        # Initialize boundary conditions
        for i in range(m + 1):
            mps[i][0] = float("inf")
        for j in range(n + 1):
            mps[0][j] = float("inf")
        mps[0][1] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                mps[i][j] = min(mps[i - 1][j], mps[i][j - 1]) + grid[i - 1][j - 1]

        return mps[m][n]


class Solution2:  # With O(1) Space
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Initialize boundary conditions
        for i in range(m):
            if i > 0:
                grid[i][0] = grid[i - 1][0] + grid[i][0]
        for j in range(n):
            if j > 0:
                grid[0][j] = grid[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[m - 1][n - 1]





