"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution_DFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid, r, c):
            nr = len(grid)
            nc = len(grid[0])

            if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)

        if grid is None or len(grid) == 0:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0
        r = 0
        while r < nr:
            c = 0
            while c < nc:
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(grid, r, c)
                c += 1
            r += 1

        return num_islands
