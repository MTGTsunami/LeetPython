"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False

        summ = sum(nums)
        if summ % k != 0:
            return False

        nums.sort(reverse=True)
        target = [summ / k] * k

        def dfs(idx):
            if idx == len(nums):
                return True

            for i in range(k):
                if target[i] >= nums[idx]:
                    target[i] -= nums[idx]
                    if dfs(idx + 1):
                        return True
                    target[i] += nums[idx]
            return False

        return dfs(0)



