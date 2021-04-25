"""
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""

from collections import deque
import copy


class MySolutionBFS(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        queue = deque([(board[0] + board[1], 0)])
        visited = set()
        visited.add(tuple(board[0] + board[1]))

        while queue:
            state, step = queue.popleft()
            if state == [1, 2, 3, 4, 5, 0]:
                return step
            idx = state.index(0)
            #  deepcopy非常费时：Runtime: 200 ms， Memory Usage: 11.8 MB
            # left, right, updown = copy.deepcopy(state), copy.deepcopy(state), copy.deepcopy(state)
            # 直接遍历赋值更快：Runtime: 28 ms, faster than 94.35%， Memory Usage: 11.5 MB, less than 100.00%
            left, right, updown = [i for i in state], [i for i in state], [i for i in state]
            if idx != 0 and idx != 3:
                left[idx], left[idx - 1] = left[idx - 1], left[idx]
                if tuple(left) not in visited:
                    visited.add(tuple(left))
                    queue.append((left, step + 1))

            if idx != 2 and idx != 5:
                right[idx], right[idx + 1] = right[idx + 1], right[idx]
                if tuple(right) not in visited:
                    visited.add(tuple(right))
                    queue.append((right, step + 1))

            if idx <= 2:
                updown[idx], updown[idx + 3] = updown[idx + 3], updown[idx]
            else:
                updown[idx], updown[idx - 3] = updown[idx - 3], updown[idx]
            if tuple(updown) not in visited:
                visited.add(tuple(updown))
                queue.append((updown, step + 1))

        return -1


class Solution(object):  # Python2 A* search
    def slidingPuzzle(self, board):
        R, C = len(board), len(board[0])
        start = tuple(itertools.chain(*board))
        target = tuple(range(1, R*C) + [0])
        target_wrong = tuple(range(1, R*C-2) + [R*C-1, R*C-2, 0])
        pq = [(0, 0, start, start.index(0))]
        cost = {start: 0}

        expected = {(C*r+c+1) % (R*C) : (r, c)
                    for r in range(R) for c in range(C)}
        def heuristic(board):
            ans = 0
            for r in range(R):
                for c in range(C):
                    val = board[C*r + c]
                    if val == 0: continue
                    er, ec = expected[val]
                    ans += abs(r - er) + abs(c - ec)
            return ans

        while pq:
            #f = estimated distance (priority)
            #g = actual distance travelled (depth)
            f, g, board, zero = heapq.heappop(pq)
            if board == target: return g
            if board == target_wrong: return -1
            if f > cost[board]: continue

            for delta in (-1, 1, -C, C):
                nei = zero + delta
                if abs(zero / C - nei / C) + abs(zero % C - nei % C) != 1:
                    continue
                if 0 <= nei < R*C:
                    board2 = list(board)
                    board2[zero], board2[nei] = board2[nei], board2[zero]
                    board2t = tuple(board2)
                    ncost = g + 1 + heuristic(board2t)
                    if ncost < cost.get(board2t, float('inf')):
                        cost[board2t] = ncost
                        heapq.heappush(pq, (ncost, g+1, board2t, nei))

        return -1