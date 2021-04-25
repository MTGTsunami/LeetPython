"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class MySolution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == 0 or num2 == 0:
            return "0"

        n, m = len(num1), len(num2)
        if n < m:
            return self.multiply(num2, num1)

        total = 0
        for i in range(m - 1, -1, -1):
            count = 0
            for j in range(n - 1, -1, -1):
                count += int(num2[i]) * int(num1[j]) * (10 ** (n - 1 - j))
            total += count * (10 ** (m - 1 - i))
        return str(total)


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1

        for n1 in reversed(num1):
            tempPos = pos
            for n2 in reversed(num2):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos - 1] += product[tempPos] / 10
                product[tempPos] %= 10
                tempPos -= 1
            pos -= 1

        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))

