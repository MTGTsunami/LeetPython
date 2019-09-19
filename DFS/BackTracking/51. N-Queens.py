"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        def could_place(row, col):
            return not (cols[col] + dale_diagonals[row - col] + hill_diagonals[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            dale_diagonals[row - col] = 1
            hill_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            dale_diagonals[row - col] = 0
            hill_diagonals[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append("." * col + "Q" + "." * (n - col - 1))
            ans.append(solution)

        cols = [0] * n  # control the whole column restriction
        dale_diagonals = [0] * (2 * n - 1)  # control the whole dale diagonals restriction
        hill_diagonals = [0] * (2 * n - 1)  # control the whole hill diagonals restriction
        queens = set()
        ans = []
        backtrack()
        return ans
