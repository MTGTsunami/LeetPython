"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rlist = []
        n = len(nums)
        if n == 0:
            return rlist

        for i in range(n):
            index = abs(nums[i])
            if index == n:
                nums[0] = -abs(nums[0])
            else:
                nums[index] = -abs(nums[index])

        for j in range(1, n):
            if nums[j] > 0:
                rlist.append(j)
        if nums[0] > 0:
            rlist.append(n)
        return rlist