"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class MySolution:  # The input can be minus
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        minus = False
        if numerator * denominator < 0:
            minus = True
        if minus:
            if numerator < 0:
                numerator = -numerator
            else:
                denominator = -denominator

        res = ""
        quo, rem = divmod(numerator, denominator)
        if rem != 0:
            res += str(quo) + '.'
        else:
            res += str(quo)

        visitedSet = set()
        visitedList = []
        decimal = ""
        while rem not in visitedSet and rem != 0:
            visitedSet.add(rem)
            visitedList.append(rem)
            quo, rem = divmod(rem * 10, denominator)
            decimal += str(quo)

        if rem == 0:
            return res + decimal if not minus else '-' + res + decimal
        else:
            idx = visitedList.index(rem)
            return res + decimal[:idx] + '(' + decimal[idx:] + ')' if not minus \
                else '-' + res + decimal[:idx] + '(' + decimal[idx:] + ')'
