"""
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.



Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0


Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4
"""


class MySolution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        beginMax, endMax = float("-inf"), float("-inf")
        total1, total2 = 0, 0
        curr_max, sub_max = 0, float("-inf")

        for i in range(len(arr)):
            total1 += arr[i]
            total2 += arr[len(arr) - 1 - i]
            beginMax = max(beginMax, total1)
            endMax = max(endMax, total2)
            curr_max = max(arr[i] + curr_max, arr[i])
            sub_max = max(curr_max, sub_max)

        if k == 1:
            return sub_max % (10 ** 9 + 7)

        if total1 > 0:
            return max(sub_max, beginMax + (k - 2) * total1 + endMax) % (10 ** 9 + 7)
        else:
            ans = max(sub_max, beginMax + endMax)
            return ans % (10 ** 9 + 7) if ans >= 0 else 0


