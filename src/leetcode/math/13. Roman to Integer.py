"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII,
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    count = 0
    if "CM" in s:
        s = s.replace("CM", '')
        count += 900
    if "CD" in s:
        s = s.replace("CD", '')
        count += 400
    if "XC" in s:
        s = s.replace("XC", '')
        count += 90
    if "XL" in s:
        s = s.replace("XL", '')
        count += 40
    if "IX" in s:
        s = s.replace("IX", '')
        count += 9
    if "IV" in s:
        s = s.replace("IV", '')
        count += 4
    if s == '':
        return count

    while s != '':
        if 'M' in s:
            count += 1000
            s = s.replace('M', '', 1)
        elif 'D' in s:
            count += 500
            s = s.replace('D', '', 1)
        elif 'C' in s:
            count += 100
            s = s.replace('C', '', 1)
        elif 'L' in s:
            count += 50
            s = s.replace('L', '', 1)
        elif 'X' in s:
            count += 10
            s = s.replace('X', '', 1)
        elif 'V' in s:
            count += 5
            s = s.replace('V', '', 1)
        elif 'I' in s:
            count += 1
            s = s.replace('I', '', 1)
    return count  # accepted


print(romanToInt("IV"))