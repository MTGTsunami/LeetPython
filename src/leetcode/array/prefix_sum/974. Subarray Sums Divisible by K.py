"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.



Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""

from collections import Counter


class Solution(object):  # module prefix sum O(n)
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        p = [0]
        for x in A:
            p.append((p[-1] + x) % K)

        c = Counter(p)
        return sum(v * (v - 1) / 2 for v in c.values())  # Combination


class MySolution(object):  # Common prefix sum O(n^2)
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count, ans = 0, 0
        for i, num in enumerate(A):
            count += num
            if count % K == 0:
                ans += 1
            A[i] = count

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if (A[j] - A[i]) % K == 0:
                    ans += 1
        return ans