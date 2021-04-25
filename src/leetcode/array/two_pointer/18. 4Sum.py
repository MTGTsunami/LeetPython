"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        check = {}
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1, n-2):
                ptr1 = j + 1
                ptr2 = n - 1
                while ptr2 > ptr1:
                    sum = nums[i] + nums[j] + nums[ptr1] + nums[ptr2]
                    if sum == target:
                        if (nums[i], nums[j], nums[ptr1], nums[ptr2]) in check:
                            ptr1 += 1
                            ptr2 -= 1
                        else:
                            check[(nums[i], nums[j], nums[ptr1], nums[ptr2])] = 0
                            result.append([nums[i], nums[j], nums[ptr1], nums[ptr2]])
                            ptr1 += 1
                            ptr2 -= 1
                    elif sum < target:
                        ptr1 += 1
                    else:
                        ptr2 -= 1
        return result