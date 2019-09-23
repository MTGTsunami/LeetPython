"""
Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.


Example 1:
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984


Constraints:

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
It's guaranteed that the result will be in range [1, 2 * 10^9]
"""

import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)

        def count(val, a, b, c):
            return val//a + val//b + val//c - val//lcm(a, b)-val//lcm(a, c)-val//lcm(c, b) + val//lcm(lcm(a, b), c)
        l = 1
        r = max([a, b, c]) * n
        tmp = (l+r)//2
        while count(tmp, a, b, c) != n-1:
            if count(tmp, a, b, c) > n-1:
                r = tmp
            else:
                l = tmp
            tmp = (l+r)//2
        while count(tmp, a, b, c) != n:
            tmp += 1
        return tmp


