"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class BestSolution:  # O(m+n)
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])

        row, col = m - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False


class MySolution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        if len(matrix) == 1:
            if target > matrix[0][len(matrix[0])-1] or target < matrix[0][0]:
                return False
            else:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if target == matrix[0][mid]:
                        return True
                    elif target > matrix[0][mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
        else:
            colmid = (len(matrix) - 1) // 2
            if self.searchMatrix(matrix[:colmid+1], target) or self.searchMatrix(matrix[colmid+1:], target):
                return True
            return False


class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)