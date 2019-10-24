"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""


class FenwickTree:
    def __init__(self, n):
        self.FTree = [0] * (n + 1)  # frequency of the appearence

    def update(self, i, delta):
        while i < len(self.FTree):
            self.FTree[i] += delta
            i += (i & -i)

    def query(self, i):
        sumAll = 0
        while i > 0:
            sumAll += self.FTree[i]
            i -= (i & -i)
        return sumAll


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ranks, rank = {}, 1
        for num in sorted(nums):
            if num not in ranks:
                ranks[num] = rank
                rank += 1

        BITree = FenwickTree(len(ranks))

        res = []
        for num in reversed(nums):
            res.append(BITree.query(ranks[num] - 1))
            BITree.update(ranks[num], 1)
        return reversed(res)
