"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        def findPivot(nums):
            if len(nums) == 2:
                if nums[0] > nums[1]:
                    return 1
                else:
                    return 2

            mid = int((0 + len(nums) - 1) / 2)
            if nums[mid] > nums[0]:
                return mid + findPivot(nums[mid:])
            else:
                return findPivot(nums[:mid + 1])

        def binarySearch(nums, target):
            if len(nums) == 1:
                if nums[0] == target:
                    return 0
                else:
                    return -1

            mid = int((0 + len(nums) - 1) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binarySearch(nums[:mid + 1], target)
            else:
                k = binarySearch(nums[mid + 1:], target)
                if k == -1:
                    return k
                else:
                    return mid + k + 1

        pivot = findPivot(nums)
        if pivot == len(nums):
            return binarySearch(nums, target)
        else:
            index1 = binarySearch(nums[:pivot], target)
            index2 = binarySearch(nums[pivot:], target)
            if index1 != -1:
                return index1
            elif index2 != -1:
                return len(nums[:pivot]) + index2
            else:
                return -1