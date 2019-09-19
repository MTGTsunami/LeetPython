"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        product = 1
        countZero = 0
        for i in nums:
            if i != 0:
                product *= i
            else:
                countZero += 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if countZero > 1:
                    output.append(0)
                else:
                    output.append(product)
            else:
                if countZero == 0:
                    output.append(product/nums[i])
                else:
                    output.append(0)
        return output