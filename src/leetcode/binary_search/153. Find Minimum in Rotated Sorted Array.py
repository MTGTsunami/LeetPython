"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        base = nums[0]
        left = 0
        right = n - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            if right == left + 1:
                return min(nums[left], nums[right])

            if nums[mid] > base:
                left = mid + 1
            else:
                right = mid - 1
                if nums[right] >= base:
                    return nums[right + 1]

        return nums[left]