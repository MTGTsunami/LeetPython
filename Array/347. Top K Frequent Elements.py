"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution1(object):
    #  O(nlogn) sorting
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = collections.Counter(nums)
        ans = res.items()
        ans.sort(key=lambda x: x[1], reverse=True)

        ret = []
        count = 0
        while count < k:
            ret.append(ans[count][0])
            count += 1
        return ret


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) solution -- 2 hashtables
        count = {}
        freq = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for d, v in count.items():
            if v not in freq:
                freq[v] = [d]
            else:
                freq[v].append(d)

        ans = []
        for i in range(len(nums), 0, -1):
            if i in freq:
                for j in freq[i]:
                    ans.append(j)
        return ans[:k]
