"""
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
"""


class MySolution1:  # O(M*N)
    def shortestWay(self, source: str, target: str) -> int:
        l, r = 0, 1
        count = 0
        while r <= len(target):
            if self.isSubstring(source, target[l:r]):
                r += 1
                if r > len(target):
                    count += 1
            else:
                if r - l == 1:
                    return -1
                else:
                    count += 1
                    l = r - 1
        return count

    def isSubstring(self, source: str, s: str) -> bool:
        pt = 0
        for p in range(len(source)):
            if pt == len(s):
                return True
            if source[p] == s[pt]:
                pt += 1
        return False if pt < len(s) else True


class MySolution2:  # O(M*logN)
    def shortestWay(self, source: str, target: str) -> int:
        L, R = 0, len(target) - 1
        count = 0
        while L <= R:
            l, r = L, R
            while l <= r:
                mid = (l + r) // 2
                if self.isSubstring(source, target[L:mid + 1]):
                    l = mid + 1
                else:
                    if mid == L:
                        return -1
                    r = mid - 1
            L = r + 1
            count += 1
        return count

    def isSubstring(self, source: str, s: str) -> bool:
        pt = 0
        for p in range(len(source)):
            if pt == len(s):
                return True
            if source[p] == s[pt]:
                pt += 1
        return False if pt < len(s) else True


import bisect
from collections import defaultdict


class Solution:  # ~= O(M+N)
    def shortestWay(self, source: str, target: str) -> int:
        sourceDict = defaultdict(list)
        for i, c in enumerate(source):
            sourceDict[c].append(i)

        i, j = 0, 0
        count = 0
        while j < len(target):
            if target[j] not in sourceDict:
                return -1
            i = bisect.bisect_left(sourceDict[target[j]], i)
            if i >= len(sourceDict[target[j]]):
                count += 1
                i = 0
            else:
                i = sourceDict[target[j]][i] + 1
                j += 1
        return count + 1
