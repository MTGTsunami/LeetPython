"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

from collections import deque


class MySolution:  # BFS
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0

        queue = deque([(nums[0], 0, 0)])
        farest = -1
        while queue:
            jump, idx, steps = queue.popleft()
            if idx == len(nums) - 1:
                return steps
            if idx + jump > farest:
                for j in range(farest + 1, idx + jump + 1 if idx + jump + 1 < len(nums) else len(nums)):
                    queue.append((nums[j], j, steps + 1))
                farest = idx + jump
        return -1


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        edge, maxEdge = 0, 0
        for i in range(len(nums)):
            if i > edge:
                edge = maxEdge
                res += 1
            maxEdge = max(maxEdge, i + nums[i])
        return res
