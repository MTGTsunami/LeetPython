"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""


class FenwickTree(object):

    def __init__(self, n):
        self.BITree = [0] * (n + 1)

    def update(self, i, delta):  # update the difference between new val and old val
        while i < len(self.BITree):
            self.BITree[i] += delta
            i += (i & -i)

    def query(self, i):
        sumZeroToI = 0
        while i > 0:
            sumZeroToI += self.BITree[i]
            i -= (i & -i)
        return sumZeroToI


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.fenwick = FenwickTree(len(nums))
        for i in range(len(nums)):
            self.fenwick.update(i + 1, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.fenwick.update(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.fenwick.query(j + 1) - self.fenwick.query(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
