"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""


class MySolutionBFS:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        num = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    num += 1
                elif grid[row][col] == 2:
                    rotten.add((row, col))

        time = 0
        while rotten:
            newrotten = set()
            spread = False
            for r, c in rotten:
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    newrotten.add((r - 1, c))
                    spread = True
                    num -= 1

                if r + 1 < len(grid) and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    newrotten.add((r + 1, c))
                    spread = True
                    num -= 1

                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    newrotten.add((r, c - 1))
                    spread = True
                    num -= 1

                if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    newrotten.add((r, c + 1))
                    spread = True
                    num -= 1

            if spread:
                time += 1
            rotten = newrotten

        if num != 0:
            return -1
        else:
            return time