"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""


class MySolution(object):  # Sliding Window
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        minlen = float("inf")
        l, length, currSum = 0, 0, 0
        for r in range(len(nums)):
            currSum += nums[r]
            length += 1
            if currSum >= s:
                while currSum >= s:
                    currSum -= nums[l]
                    length -= 1
                    l += 1
                minlen = min(minlen, length + 1)
        return minlen if minlen != float("inf") else 0
