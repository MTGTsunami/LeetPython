"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Dp solution. O(amount * # coins)
        if amount == 0:
            return 0

        # Initialize the array
        p = [float('inf') for _ in range(amount + 1)]
        p[0] = 0  # When amount is 0, total number of coins is 0
        if 1 in coins:
            p[1] = 1

        for i in range(2, amount + 1):
            min = float('inf')
            for j in coins:
                if i - j >= 0:
                    if p[i - j] < min:
                        min = p[i - j]
            if min != float('inf'):
                p[i] = min + 1

        if p[amount] == float('inf'):
            return -1
        else:
            return p[amount]

