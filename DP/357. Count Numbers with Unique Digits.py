"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99
"""


class MySolution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            digit = 1
            while digit < i + 1:
                if digit == 1:
                    dp[i] *= 9
                else:
                    dp[i] *= 11 - digit
                digit += 1
            dp[i] += dp[i - 1]
        return dp[n]

