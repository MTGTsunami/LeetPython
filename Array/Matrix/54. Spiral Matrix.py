"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rlist = []
        if not matrix:
            return rlist

        row = len(matrix)
        col = len(matrix[0])

        i = 0  # Number of elements
        layer = 1
        right = 0  # Starting point
        down = 0  # Starting point
        flag = 1  # The status of moving
        while i < row * col:

            # Going right
            if flag == 1:
                if right < col - layer:  # When the rightmost is not reached yet...
                    rlist.append(matrix[down][right])
                    right += 1
                else:
                    flag = 2  # It's time to go down!
                    left = right

            # Going down
            if flag == 2:
                if down < row - layer:  # When the bottommost is not reached yet...
                    rlist.append(matrix[down][left])
                    down += 1
                else:
                    flag = 3  # It's time to go left!
                    up = down

            # Going left
            if flag == 3:
                if left > layer - 1:  # When the leftmost is not reached yet...
                    rlist.append(matrix[up][left])
                    left -= 1
                else:
                    flag = 4  # It's time to go up!
                    right = left

            # Going up
            if flag == 4:
                if up > layer - 1:  # When the uppermost is not reached yet...
                    rlist.append(matrix[up][right])
                    up -= 1
                else:
                    flag = 1  # It's time to go right again!
                    down = up + 1  # Setting the starting position for the next layer
                    right = left + 1
                    layer += 1  # Updating the layer number
                    i -= 1  # For every i, you need to append an element from the matrix to the rlist

            i += 1

            # If there is only one number left in the final layer
            if i == (row * col - 1) and row == col and row % 2 == 1:
                rlist.append(matrix[row // 2][col // 2])
                break

        return rlist