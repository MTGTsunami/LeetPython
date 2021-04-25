"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""


class MySolution(object):  # O(n) space
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxrob = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                maxrob.append(nums[0])
            elif i == 1:
                maxrob.append(max(nums[0], nums[1]))
            else:
                maxrob.append(max(maxrob[i - 2] + nums[i], maxrob[i - 1]))
        return maxrob[-1]


class StandardSolution(object):  # O(1) space
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        premax = 0
        currmax = 0
        for num in nums:
            temp = currmax
            currmax = max(premax + num, currmax)
            premax = temp
        return currmax