"""
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.



Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4


Constraints:

2 <= arr.length <= 40
1 <= arr[i] <= 15
It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).
"""


class MySolution(object):  # dp O(n^3) time, O(n^2) space
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        largest = [[float("-inf")] * len(arr) for _ in range(len(arr))]
        dp = [[0] * len(arr) for _ in range(len(arr))]

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if i == j:
                    largest[i][j] = arr[j]
                else:
                    largest[i][j] = max(largest[i][j - 1], arr[j])

        for i in range(len(arr) - 2, -1, -1):
            for j in range(i + 1, len(arr)):
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] + largest[i][k] * largest[k + 1][j] for k in range(i, j))
        return dp[0][-1]


class Solution(object):  # with stack, O(n) time
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        stack = [float('inf')]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res


