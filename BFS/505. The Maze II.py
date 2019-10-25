"""
There is a ball in a maze with empty spaces and walls.
The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall.
When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination.
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).
If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array.
1 means the wall and 0 means the empty space.
You may assume that the borders of the maze are all walls.
The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.


Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""


class SolutionDFS(object):  # TLE
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        distance = [[float("inf")] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0
        self.dfs(maze, start, distance)
        return distance[destination[0]][destination[1]] \
            if distance[destination[0]][destination[1]] != float("inf") else -1

    def dfs(self, maze, start, distance):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di in directions:
            x = start[0] + di[0]
            y = start[1] + di[1]
            count = 0

            while 0 <= y < len(maze[0]) and 0 <= x < len(maze) and maze[x][y] == 0:
                x += di[0]
                y += di[1]
                count += 1

            if distance[start[0]][start[1]] + count < distance[x - di[0]][y - di[1]]:
                distance[x - di[0]][y - di[1]] = distance[start[0]][start[1]] + count
                self.dfs(maze, [x - di[0], y - di[1]], distance)


from collections import deque


class SolutionBFS(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        distance = [[float("inf")] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([start])
        while queue:
            s = queue.popleft()
            for d in directions:
                x = s[0] + d[0]
                y = s[1] + d[1]
                count = 0
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += d[0]
                    y += d[1]
                    count += 1
                if distance[s[0]][s[1]] + count < distance[x - d[0]][y - d[1]]:
                    distance[x - d[0]][y - d[1]] = distance[s[0]][s[1]] + count
                    queue.append([x - d[0], y - d[1]])
        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float("inf") else -1


