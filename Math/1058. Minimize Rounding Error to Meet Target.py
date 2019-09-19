"""
Given an array of prices [p1,p2...,pn] and a target, round each price pi to Roundi(pi) so that the rounded array [Round1(p1),Round2(p2)...,Roundn(pn)] sums to the given target. Each operation Roundi(pi) could be either Floor(pi) or Ceil(pi).

Return the string "-1" if the rounded array is impossible to sum to target. Otherwise, return the smallest rounding error, which is defined as Σ |Roundi(pi) - (pi)| for i from 1 to n, as a string with three places after the decimal.



Example 1:

Input: prices = ["0.700","2.800","4.900"], target = 8
Output: "1.000"
Explanation:
Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 .
Example 2:

Input: prices = ["1.500","2.500","3.500"], target = 10
Output: "-1"
Explanation:
It is impossible to meet the target.


Note:

1 <= prices.length <= 500.
Each string of prices prices[i] represents a real number which is between 0 and 1000 and has exactly 3 decimal places.
target is between 0 and 1000000.
"""

from decimal import *


class MySolution(object):  # Greedy
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
        largest, smallest = 0, 0
        for i in range(len(prices)):
            price = Decimal(prices[i])
            smallest += int(price)
            largest += (int(price) + 1) if int(price) != price else int(price)
            prices[i] = Decimal(int(price) + 1) - price if int(price) != price else Decimal("0.000")

        if target > largest or target < smallest:
            return str(-1)
        largest -= target  # Count as the number of downs
        smallest = len(prices) - largest  # Count as the number of ups
        prices.sort()
        ans, count = 0, 0
        for err in prices:
            if count < smallest:
                ans += err
                count += 1
            else:
                ans += (1 - err)
        return str(ans)
