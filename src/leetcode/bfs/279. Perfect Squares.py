"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class MySolution(object):  # A little bit larger than O(n) time
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square = [float("inf")] * n
        for i in range(1, n + 1):
            sqrt = i ** 0.5
            floor = int(sqrt)
            if sqrt - floor == 0:
                square[i - 1] = 1
                nearest = floor
            else:
                while floor >= 1:
                    square[i - 1] = min(square[i - floor ** 2 - 1] + 1, square[i - 1])
                    floor -= 1
        return square[-1]


class SolutionDP(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square = [float("inf")] * (n + 1)
        square[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                square[i] = min(square[i - j * j] + 1, square[i])
                j += 1
        return square[-1]


class SolutionMath(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        def isSquare(n):
            return (n ** 0.5 - int(n ** 0.5)) == 0

        #  Based on Lagrange's Four Square theorem, there
        #  are only 4 possible results: 1, 2, 3, 4.

        #  If n is a perfect square, return 1.
        if isSquare(n):
            return 1

        #  The result is 4 if and only if n can be written in the form of 4^k*(8*m + 7).
        #  Please refer to Legendre's four-square theorem.
        while n % 4 == 0:
            n /= 4

        if n % 8 == 7:
            return 4

        for i in range(1, int(n ** 0.5) + 1):
            if isSquare(n - i * i):
                return 2

        return 3


class SolutionBFS(object):  # Important
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        depth = 0
        nodes = set([n])
        edges = [i * i for i in range(1, int(n ** 0.5) + 1)]
        while True:
            depth += 1
            nextLevel = set()
            for node in nodes:
                for edge in edges:
                    if edge == node:
                        return depth
                    elif edge < node:
                        nextLevel.add(node - edge)
                    else:
                        break
            nodes = nextLevel
