"""
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.
Note: The value of n won't exceed 100,000.
"""


class MySolution:  # backtracking TLE
    def checkRecord(self, n: int) -> int:
        def backtracking(idx, expr, countA):
            if idx == n:
                s = "".join(expr)
                res.append(s)
            else:
                for ch in attendence:
                    if ch == "A":
                        countA += 1
                    if not (countA == 2 or (ch == "L" and expr[-2:] == ["L", "L"])):
                        expr.append(ch)
                        backtracking(idx + 1, expr, countA)
                        expr.pop()
                    if ch == "A":
                        countA -= 1

        attendence, res = ["A", "P", "L"], []
        backtracking(0, [], 0)
        return len(res)


class Solution:  # DP
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 0

        # string with only P and L, dp[n] denotes the number of strings of len n
        dpPL = [1, 2, 4]
        for i in range(3, n + 1):
            dpPL.append((dpPL[i - 3] + dpPL[i - 2] + dpPL[i - 1]) % 1000000007)
        res = dpPL[n]
        for i in range(n):
            res += (dpPL[i] * dpPL[n - 1 - i]) % 1000000007
        return res % 1000000007

