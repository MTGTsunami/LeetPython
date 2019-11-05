"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

"""


class MySolution:  # O(n^2) time, two pointer
    def find132pattern(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            leftmin, rightmax = float("inf"), float("-inf")
            for l in range(i - 1, -1, -1):
                if nums[l] < nums[i]:
                    leftmin = min(leftmin, nums[l])
            for r in range(i + 1, len(nums)):
                if nums[r] < nums[i]:
                    rightmax = max(rightmax, nums[r])
            if leftmin < rightmax:
                return True
        return False


class Solution(object):  # O(n) Stack
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        ak = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < ak:  # If ai < ak
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    ak = stack.pop()
                stack.append(nums[i])
        return False
