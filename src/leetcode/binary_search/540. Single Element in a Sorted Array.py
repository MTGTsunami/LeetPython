"""
Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once. Find this single element that appears only once.



Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.
"""


class MySolution1:  # bit manipulation
    def singleNonDuplicate(self, nums: List[int]) -> int:
        a = nums[0]
        for num in nums[1:]:
            a ^= num
        return a


class Solution2:  # Binary search
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def isOdd(l):
            return len(l) % 2 == 1

        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if isOdd(nums[left:mid]):
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                elif nums[mid] == nums[mid + 1]:
                    right = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    right = mid
                elif nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    return nums[mid]
        return nums[left]