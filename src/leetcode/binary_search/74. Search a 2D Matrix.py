"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class MySolution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = [0, 0], [m - 1, n - 1]
        while (left[0] == right[0] and left[1] <= right[1]) or left[0] < right[0]:
            mid = self.findMedian(left, right, matrix)
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] < target:
                if mid[1] == n - 1:
                    left[0], left[1] = mid[0] + 1, 0
                else:
                    left[0], left[1] = mid[0], mid[1] + 1
            else:
                if mid[1] == 0:
                    right[0], right[1] = mid[0] - 1, n - 1
                else:
                    right[0], right[1] = mid[0], mid[1] - 1
        return False

    def findMedian(self, left, right, matrix):
        row, col = len(matrix), len(matrix[0])
        if left[1] <= right[1]:
            total = right[1] - left[1] + 1 + (right[0] - left[0]) * col
        else:
            total = col - left[1] + right[1] + 1 + (right[0] - left[0] - 1) * col
        steps = (total + 1) // 2
        if steps <= col - left[1]:
            mid = [left[0], left[1] + steps - 1]
        else:
            steps -= col - left[1]
            newrow, newcol = divmod(steps, col)
            if newcol == 0:
                mid = [left[0] + newrow, col - 1]
            else:
                mid = [left[0] + newrow + 1, newcol - 1]
        return mid


class Solution:  # Faster binary search
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False