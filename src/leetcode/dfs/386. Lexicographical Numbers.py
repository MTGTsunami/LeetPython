"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def dfs(k, out):
            if k <= n:
                out.append(k)
            m = 10 * k
            if m <= n:
                for i in range(10):
                    dfs(m + i, out)

        out = []
        for i in range(1, 10):
            dfs(i, out)
        return out
