"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution:  #  Divide and Conquer
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            mid = int((length - 1) / 2)
            leftproduct = self.maxProduct(nums[:mid + 1])
            rightproduct = self.maxProduct(nums[mid + 1:])
            crossproduct = self.maxCrossProduct(nums, mid)
            if leftproduct >= rightproduct and leftproduct >= crossproduct:
                return leftproduct
            elif rightproduct >= leftproduct and rightproduct >= crossproduct:
                return rightproduct
            else:
                return crossproduct

    def maxCrossProduct(self, nums, mid):
        """
        :type nums: List[int]
        :type mid: int
        :rtype: int
        """
        leftmaxproduct = -float('inf')
        leftminproduct = float('inf')
        product = 1
        for i in nums[mid::-1]:
            product *= i
            if product > leftmaxproduct:
                leftmaxproduct = product
            if product < leftminproduct:
                leftminproduct = product

        rightmaxproduct = -float('inf')
        rightminproduct = float('inf')
        product = 1
        for j in nums[mid + 1:]:
            product *= j
            if product > rightmaxproduct:
                rightmaxproduct = product
            if product < rightminproduct:
                rightminproduct = product

        if leftminproduct * rightminproduct > leftmaxproduct * rightmaxproduct:
            return leftminproduct * rightminproduct
        else:
            return leftmaxproduct * rightmaxproduct
