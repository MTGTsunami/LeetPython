"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""

from collections import defaultdict


class MySolution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        countX, countO = 0, 0
        X, O = defaultdict(list), defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    countX += 1
                    X[i].append(j)
                    X[j + 3].append(i)
                elif board[i][j] == "O":
                    countO += 1
                    O[i].append(j)
                    O[j + 3].append(i)

        if countX - countO > 1 or countO > countX:
            return False

        Xwin = False
        for v in X.values():
            if len(v) == 3:
                Xwin = True
        if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or \
                (board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X"):
            Xwin = True

        Owin = False
        for v in O.values():
            if len(v) == 3:
                Owin = True
        if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or \
                (board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O"):
            Owin = True

        if Owin and Xwin:
            return False
        if (Xwin and countX == countO) or (Owin and countX - countO == 1):
            return False
        return True
