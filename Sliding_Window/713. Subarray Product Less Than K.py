"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""


class MySolution(object):  # Sliding window
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0 or k == 1:
            return 0

        r = 0
        count, temp = 0, 1
        end = False
        for l in range(len(nums)):
            if r < l:
                r = l
            while temp < k and r < len(nums):
                temp *= nums[r]
                r += 1
                if r >= len(nums):
                    end = True
                    break
            if not end:
                r -= 1
                temp /= nums[r]
            else:
                if temp >= k:
                    r -= 1
                    end = False
                    temp /= nums[r]
            count += (r - l)
            if r != l:
                temp /= nums[l]
        return count


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

