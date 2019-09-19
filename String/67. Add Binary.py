"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = len(a)
        m = len(b)
        if n < m:
            return self.addBinary(b, a)

        b = "0" * (n - m) + b
        add = 0
        c = ""
        for i in range(n - 1, -1, -1):
            bit = add + int(a[i]) + int(b[i])
            if bit == 3:
                c = "1" + c
                add = 1
            elif bit == 2:
                c = "0" + c
                add = 1
            elif bit == 1:
                c = "1" + c
                add = 0
            else:
                c = "0" + c
                add = 0

        if add == 1:
            return "1" + c
        else:
            return c


