"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            i, j, val = queue.popleft()
            if i - 1 >= 0 and rooms[i - 1][j] != -1:
                if val + 1 < rooms[i - 1][j]:
                    rooms[i - 1][j] = val + 1
                    queue.append((i - 1, j, val + 1))
            if i + 1 < len(rooms) and rooms[i + 1][j] != -1:
                if val + 1 < rooms[i + 1][j]:
                    rooms[i + 1][j] = val + 1
                    queue.append((i + 1, j, val + 1))
            if j - 1 >= 0 and rooms[i][j - 1] != -1:
                if val + 1 < rooms[i][j - 1]:
                    rooms[i][j - 1] = val + 1
                    queue.append((i, j - 1, val + 1))
            if j + 1 < len(rooms[0]) and rooms[i][j + 1] != -1:
                if val + 1 < rooms[i][j + 1]:
                    rooms[i][j + 1] = val + 1
                    queue.append((i, j + 1, val + 1))
