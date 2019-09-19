"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution_Best(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 1

        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for j in range(n):
            index = abs(nums[j])
            if index == n:
                nums[0] = -abs(nums[0])
            else:
                nums[index] = -abs(nums[index])

        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1


class Solution(object):  # O(n) space
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1

        mini = min(nums)
        s = set(nums)
        if mini <= 1:
            i = 1
            while True:
                if i in s:
                    i += 1
                else:
                    return i
        else:
            return 1

