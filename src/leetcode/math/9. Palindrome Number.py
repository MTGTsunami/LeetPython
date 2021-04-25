"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            l = []
            while x % 10 != x:
                rem = x % 10
                x = (x - rem) / 10
                l.append(rem)
            l.append(x)
        n = len(l)

        i = 0
        j = n - 1
        while i <= j:
            if l[i] == l[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

