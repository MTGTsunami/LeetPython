"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""


class MySolutionDFS(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """

        # States:
        # 0 stands for stopped state; 1 stands for going up;
        # 2 stands for going right; 3 stands for going down; 4 stands for going left
        def dfs(maze, r, c, destination, state, visited):
            if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]) or \
                    maze[r][c] == 1:
                return False

            if state == 0:
                if [r, c] == destination:
                    return True
                if (r, c) not in visited:
                    visited.add((r, c))
                    if dfs(maze, r - 1, c, destination, 1, visited) or \
                            dfs(maze, r + 1, c, destination, 3, visited) or \
                            dfs(maze, r, c - 1, destination, 4, visited) or \
                            dfs(maze, r, c + 1, destination, 2, visited):
                        return True
            elif state == 1:
                if r - 1 < 0 or maze[r - 1][c] == 1:
                    return dfs(maze, r, c, destination, 0, visited)
                else:
                    return dfs(maze, r - 1, c, destination, 1, visited)
            elif state == 2:
                if c + 1 >= len(maze[0]) or maze[r][c + 1] == 1:
                    return dfs(maze, r, c, destination, 0, visited)
                else:
                    return dfs(maze, r, c + 1, destination, 2, visited)
            elif state == 3:
                if r + 1 >= len(maze) or maze[r + 1][c] == 1:
                    return dfs(maze, r, c, destination, 0, visited)
                else:
                    return dfs(maze, r + 1, c, destination, 3, visited)
            else:
                if c - 1 < 0 or maze[r][c - 1] == 1:
                    return dfs(maze, r, c, destination, 0, visited)
                else:
                    return dfs(maze, r, c - 1, destination, 4, visited)

        return dfs(maze, start[0], start[1], destination, 0, set())


class SolutionDFS_simplified(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """

        # States:
        # 0 stands for stopped state; 1 stands for going up;
        # 2 stands for going right; 3 stands for going down; 4 stands for going left
        def dfs(r, c, state, visited):
            if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]) or \
                    maze[r][c] == 1:
                return False

            if state == 0:
                if [r, c] == destination:
                    return True
                if (r, c) not in visited:
                    visited.add((r, c))
                    if dfs(r - 1, c, 1, visited) or \
                            dfs(r + 1, c, 3, visited) or \
                            dfs(r, c - 1, 4, visited) or \
                            dfs(r, c + 1, 2, visited):
                        return True
            elif state == 1:
                if r - 1 < 0 or maze[r - 1][c] == 1:
                    return dfs(r, c, 0, visited)
                else:
                    return dfs(r - 1, c, 1, visited)
            elif state == 2:
                if c + 1 >= len(maze[0]) or maze[r][c + 1] == 1:
                    return dfs(r, c, 0, visited)
                else:
                    return dfs(r, c + 1, 2, visited)
            elif state == 3:
                if r + 1 >= len(maze) or maze[r + 1][c] == 1:
                    return dfs(r, c, 0, visited)
                else:
                    return dfs(r + 1, c, 3, visited)
            else:
                if c - 1 < 0 or maze[r][c - 1] == 1:
                    return dfs(r, c, 0, visited)
                else:
                    return dfs(r, c - 1, 4, visited)

        return dfs(start[0], start[1], 0, set())


from collections import deque


class MySolutionBFS(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        queue = deque([tuple(start)])
        visited = set()
        while queue:
            pos = queue.popleft()
            if list(pos) == destination:
                return True

            visited.add(pos)
            r, c = pos[0], pos[1]
            row, col = r, c
            while r - 1 >= 0 and maze[r - 1][c] == 0:
                r -= 1
            if (r, c) not in visited:
                queue.append((r, c))

            r = row
            while r + 1 < len(maze) and maze[r + 1][c] == 0:
                r += 1
            if (r, c) not in visited:
                queue.append((r, c))

            r = row
            while c - 1 >= 0 and maze[r][c - 1] == 0:
                c -= 1
            if (r, c) not in visited:
                queue.append((r, c))

            c = col
            while c + 1 < len(maze[0]) and maze[r][c + 1] == 0:
                c += 1
            if (r, c) not in visited:
                queue.append((r, c))

        return False