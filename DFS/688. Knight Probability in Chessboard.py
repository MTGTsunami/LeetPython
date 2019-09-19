"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.







Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.



Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.


Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
"""


class MySolution:  # simple DFS, TLE at case 11
    def __init__(self):
        self.out = 0

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        def dfs(r, c, step, p):
            if step == K:
                self.out += p
                return
            if r - 2 >= 0 and c - 1 >= 0:
                dfs(r - 2, c - 1, step + 1, p * float(1 / 8))
            if r - 1 >= 0 and c - 2 >= 0:
                dfs(r - 1, c - 2, step + 1, p * float(1 / 8))
            if r - 2 >= 0 and c + 1 < N:
                dfs(r - 2, c + 1, step + 1, p * float(1 / 8))
            if r - 1 >= 0 and c + 2 < N:
                dfs(r - 1, c + 2, step + 1, p * float(1 / 8))
            if r + 1 < N and c - 2 >= 0:
                dfs(r + 1, c - 2, step + 1, p * float(1 / 8))
            if r + 2 < N and c - 1 >= 0:
                dfs(r + 2, c - 1, step + 1, p * float(1 / 8))
            if r + 2 < N and c + 1 < N:
                dfs(r + 2, c + 1, step + 1, p * float(1 / 8))
            if r + 1 < N and c + 2 < N:
                dfs(r + 1, c + 2, step + 1, p * float(1 / 8))

        dfs(r, c, 0, 1)
        return self.out


class Solution:  # DFS with memorization. 某一步中两个点走到了同一点上的情况可以合并

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        memo = {}
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))

        def dfs(k, x, y, P):
            p = 0
            if 0 <= x < N and 0 <= y < N:  # a valid position on the board
                if k < K:
                    for dx, dy in moves:
                        x_next, y_next = x + dx, y + dy
                        if (x_next, y_next, k + 1) not in memo:
                            memo[(x_next, y_next, k + 1)] = dfs(k + 1, x_next, y_next, P / 8)
                        p += memo[(x_next, y_next, k + 1)]
                else:  # k==K, this is the last move
                    p = P
            return p

        return dfs(0, r, c, 1.0)