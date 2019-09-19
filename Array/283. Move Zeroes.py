"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

from queue import Queue


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = Queue()
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.put(i)
            else:
                if zeros.empty():
                    continue
                else:
                    index = zeros.get()
                    nums[index] = nums[i]
                    nums[i] = 0
                    zeros.put(i)


class SolutionBetter(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = -1
        j = 0
        while j < len(nums):
            if i < j and nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
