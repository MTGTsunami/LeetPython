"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class SolutionBest(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or len(board) == 0:
            return False

        row = len(board)
        column = len(board[0])
        length = len(word)

        def dfs(r, c, i, visited):
            if i == length:  # DFS completed
                return True

            nextvisited = visited + [(r, c)]

            if r != 0 and board[r - 1][c] == word[i] and (r - 1, c) not in visited and dfs(r - 1, c, i + 1,
                                                                                           nextvisited):
                return True
            if r != row - 1 and board[r + 1][c] == word[i] and (r + 1, c) not in visited and dfs(r + 1, c, i + 1,
                                                                                                 nextvisited):
                return True
            if c != 0 and board[r][c - 1] == word[i] and (r, c - 1) not in visited and dfs(r, c - 1, i + 1,
                                                                                           nextvisited):
                return True
            if c != column - 1 and board[r][c + 1] == word[i] and (r, c + 1) not in visited and dfs(r, c + 1, i + 1,
                                                                                                    nextvisited):
                return True

        for r in range(row):
            for c in range(column):
                if board[r][c] == word[0] and dfs(r, c, 1, []):
                    return True
        return False


class SolutionBad(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(r, c, i):
            if i > len(word):
                return True

            if r - 1 >= 0:
                if board[r - 1][c] == word[i]:
                    up = dfs(r - 1, c, i + 1)
                else:
                    up = False
            else:
                up = False

            if r + 1 < row:
                if board[r + 1][c] == word[i]:
                    down = dfs(r + 1, c, i + 1)
                else:
                    down = False
            else:
                down = False

            if c - 1 >= 0:
                if board[r][c - 1] == word[i]:
                    left = dfs(r, c - 1, i + 1)
                else:
                    left = False
            else:
                left = False

            if c + 1 < column:
                if board[r][c + 1] == word[i]:
                    right = dfs(r, c + 1, i + 1)
                else:
                    right = False
            else:
                right = False

            if (up or down or left or right) is False:
                return False
            else:
                return True

        if board == None or len(board) == 0:
            return False

        row = len(board)
        column = len(board[0])

        for r in range(row):
            for c in range(column):
                i = 0
                if board[r][c] == word[i]:
                    i = i + 1
                    if dfs(r, c, i):
                        return True

        return False