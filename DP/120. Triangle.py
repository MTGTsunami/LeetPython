"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # let path(i,j) denote the minimum path from the top to floor i element j.
        # path(i,j) = min(path(i-1,j-1), path(i-1,j)) + triangle[i][j-1]
        # boundary conditions are path(0,1) = triangle[0][0], path(i,0) = inf, path(i,i+2) = inf
        # goal is to find min(path(n-1,j))

        n = len(triangle)
        path = [[0] * (n + 2) for _ in range(n)]  # initialize array "path"
        """
        path = [[] for i in range(n)]
        for i in range(n):  # initialize array "path"
            for j in range(i + 3):
                path[i].append(0)
        """

        path[0][1] = triangle[0][0]  # initialize boundary conditions
        for i in range(n):
            path[i][0] = float("inf")
            path[i][i + 2] = float("inf")

        for i in range(n):
            for j in range(1, i + 2):
                path[i][j] = min(path[i - 1][j - 1], path[i - 1][j]) + triangle[i][j - 1]

        minpath = path[n - 1][1]
        for j in range(2, n + 1):
            if path[n - 1][j] < minpath:
                minpath = path[n - 1][j]

        return minpath

