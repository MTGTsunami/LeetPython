"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class MySolution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        out = []
        out.append(self.findPosition(nums, target, "First"))
        out.append(self.findPosition(nums, target, "Last"))
        return out

    def findPosition(self, nums, target, pos):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if pos == "First":
                    if mid - 1 < 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                elif pos == "Last":
                    if mid + 1 >= len(nums) or nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
