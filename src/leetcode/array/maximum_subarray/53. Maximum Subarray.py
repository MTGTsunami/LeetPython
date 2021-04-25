"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:  # Divide and Conquer
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            mid = int((length - 1) / 2)
            leftsum = self.maxSubArray(nums[:mid + 1])
            rightsum = self.maxSubArray(nums[mid + 1:])
            crosssum = self.maxCrossSubArray(nums, mid)
            if leftsum >= rightsum and leftsum >= crosssum:
                return leftsum
            elif rightsum >= leftsum and rightsum >= crosssum:
                return rightsum
            else:
                return crosssum

    def maxCrossSubArray(self, nums, mid):
        """
        :type nums: List[int]
        :type mid: int
        :rtype: int
        """
        leftmaxsum = -float('inf')
        sum = 0
        for i in nums[mid::-1]:
            sum += i
            if sum > leftmaxsum:
                leftmaxsum = sum

        rightmaxsum = -float('inf')
        sum = 0
        for j in nums[mid + 1:]:
            sum += j
            if sum > rightmaxsum:
                rightmaxsum = sum
        return leftmaxsum + rightmaxsum


# The space complexity can be decreased to O(1) by changing the array dp into a int variable maxi
# which is used to save the current maximum sum of the continuous sub-array
class SolutionMyDP(object):  # O(n) space
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        temp = nums[0]

        for i in range(1, n):
            temp += nums[i]
            if temp < 0:
                dp[i] = max(dp[i - 1], temp, nums[i])
                if nums[i] > 0:
                    temp = nums[i]
            else:
                dp[i] = max(dp[i - 1], temp, nums[i])
                if temp < nums[i]:
                    temp = nums[i]
        return dp[-1]


