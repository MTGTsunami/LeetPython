"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index1 = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                exchange = nums[i - 1]
                index1 = i - 1
                break

        if index1 == -1:
            nums.reverse()
        else:
            i = index1 + 1
            while i < n:
                if nums[i] > exchange:
                    index2 = i
                i += 1

            nums[index1], nums[index2] = nums[index2], nums[index1]
            nums[index1 + 1:] = nums[n - 1: index1: -1]


