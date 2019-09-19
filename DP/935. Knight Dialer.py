"""
A chess knight can move as indicated in the chess diagram below:

 .



This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.



Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46


Note:

1 <= N <= 5000
"""


class MySolution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10

        dp = [1] * 10
        temp = [1] * 10
        for i in range(N - 1):
            temp[0] = dp[4] + dp[6]
            temp[1] = dp[8] + dp[6]
            temp[2] = dp[7] + dp[9]
            temp[3] = dp[4] + dp[8]
            temp[4] = dp[3] + dp[9] + dp[0]
            temp[6] = dp[1] + dp[7] + dp[0]
            temp[7] = dp[2] + dp[6]
            temp[8] = dp[1] + dp[3]
            temp[9] = dp[2] + dp[4]
            dp[:] = temp

        return (dp[0] + dp[1] + dp[2] + dp[3] + dp[4] + dp[6] + dp[7] + dp[8] + dp[9]) % (10 ** 9 + 7)

