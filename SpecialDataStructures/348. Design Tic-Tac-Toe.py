"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
"""


class MyTicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col] = player
        if player == 1 and self.wins(self.board, row, col, player):
            return 1
        elif player == 2 and self.wins(self.board, row, col, player):
            return 2
        else:
            return 0

    def wins(self, board, r, c, player):
        def check_row(board, r, c, player):
            for j in range(len(board)):
                if board[r][j] != player:
                    return False
            return True

        def check_col(board, r, c, player):
            for i in range(len(board[0])):
                if board[i][c] != player:
                    return False
            return True

        def check_upperleft_diag(board, r, c, player):
            tr, tc = r, c
            count = 0
            while r - 1 >= 0 and c - 1 >= 0:
                if board[r - 1][c - 1] != player:
                    return False
                r -= 1
                c -= 1
                count += 1
            r, c = tr, tc

            while r + 1 < len(board) and c + 1 < len(board[0]):
                if board[r + 1][c + 1] != player:
                    return False
                r += 1
                c += 1
                count += 1

            count += 1
            if count == len(board):
                return True
            else:
                return False

        def check_bottomleft_diag(board, r, c, player):
            tr, tc = r, c
            count = 0
            while r + 1 < len(board) and c - 1 >= 0:
                if board[r + 1][c - 1] != player:
                    return False
                r += 1
                c -= 1
                count += 1
                # print("a")
            r, c = tr, tc

            while r - 1 >= 0 and c + 1 < len(board[0]):
                if board[r - 1][c + 1] != player:
                    return False
                r -= 1
                c += 1
                count += 1
                # print("b")

            count += 1
            # print(count)
            if count == len(board):
                return True
            else:
                return False

        if check_row(board, r, c, player) or check_col(board, r, c, player) or \
                check_upperleft_diag(board, r, c, player) or check_bottomleft_diag(board, r, c, player):
            return True
        else:
            return False

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


class TicTacToe(object):

    def __init__(self, n):
        self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n

    def move(self, row, col, player):
        offset = player * 2 - 3
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
