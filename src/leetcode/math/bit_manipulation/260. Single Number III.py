"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        bits = 0
        while xor & 1 == 0:
            xor >>= 1
            bits += 1
        num0, num1 = [], []
        for i, num in enumerate(nums):
            for _ in range(bits):
                num >>= 1
            if num & 1 == 0:
                num0.append(nums[i])
            else:
                num1.append(nums[i])
        xor1 = 0
        for m in num0:
            xor1 ^= m
        xor2 = 0
        for n in num1:
            xor2 ^= n
        return [xor1, xor2]

