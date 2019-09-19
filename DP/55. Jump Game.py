"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == [] or len(nums) == 1:
            return True

        jumpOver = 0
        while 0 in nums:
            flag = 0
            idx = nums.index(0)
            for i in range(jumpOver, idx):  # started from the jump-over index
                reach = i + nums[i]
                if reach > idx or idx == len(nums) - 1:
                    jumpOver = i
                    flag = 1  # Found a i < idx that could jump over 0
                    nums[idx] = 1
                    break
            if flag == 0:
                return False
        return True