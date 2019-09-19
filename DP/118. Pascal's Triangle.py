"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rlist = [[1 for j in range(1, i + 2)] for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                rlist[i][j] = rlist[i - 1][j - 1] + rlist[i - 1][j]

        return rlist

