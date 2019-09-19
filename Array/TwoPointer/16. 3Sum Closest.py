"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        n = len(nums)
        minDist = float('inf')
        for i in range(n - 2):
            ptr1 = i + 1
            ptr2 = n - 1
            while ptr1 < ptr2:
                sum = nums[i] + nums[ptr1] + nums[ptr2]
                if sum == target:
                    return target
                else:
                    dist = abs(target - sum)
                    if dist < minDist:
                        minDist = dist
                        ans = sum

                    if sum < target:
                        ptr1 += 1
                    else:
                        ptr2 -= 1
        return ans

