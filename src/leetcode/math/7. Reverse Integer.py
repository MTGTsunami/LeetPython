"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s1 = str(x)
        l = list(s1)
        flag = False
        if l[0] == "-":
            l.remove(l[0])
            flag = True
        l.reverse()

        while len(l) != 1:
            if l[0] == '0':
                l.remove(l[0])
            else:
                break

        s2 = "".join(l)
        if flag == True:
            ans = -int(s2)
        else:
            ans = int(s2)

        if ans < -2 ** 31 or ans > 2 ** 31 - 1:
            return 0

        return ans