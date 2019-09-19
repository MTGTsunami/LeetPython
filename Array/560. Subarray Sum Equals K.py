"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


class Solution:  # Hashtable O(n)
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        count = 0
        sum = [0 for _ in range(len(nums) + 1)]
        d = dict()
        d['0'] = 1

        for i in range(1, len(nums) + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
            if str(sum[i] - k) in d:  # find sum[j] in front of s[i]
                count += d[str(sum[i] - k)]

            temp = str(sum[i])
            if temp in d:
                d[temp] += 1
            else:
                d[temp] = 1

        return count