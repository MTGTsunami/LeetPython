"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution1(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


class Solution2(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        maxcount = 0
        for num in nums:
            if num not in s:
                continue

            s.remove(num)

            count1 = 1
            while (num + count1) in s:
                s.remove(num + count1)
                count1 += 1

            count2 = 1
            while (num - count2) in s:
                s.remove(num - count2)
                count2 += 1

            length = count1 + count2 - 1
            maxcount = max(maxcount, length)

        return maxcount
