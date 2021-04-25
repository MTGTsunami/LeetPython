"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""


class SolutionDP:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = [[] for i in range(target + 1)]
        if target < candidates[0]:
            return []

        for i in range(candidates[0], target + 1):
            j = 0
            while i - candidates[j] >= 0:
                goal = i - candidates[j]
                if goal == 0:
                    ans[i].append([candidates[j]])
                elif len(ans[goal]) != 0:
                    for k in ans[goal]:
                        temp = k.copy()
                        temp.append(candidates[j])
                        temp.sort()
                        if temp not in ans[i]:
                            ans[i].append(temp)

                j += 1
                if j >= len(candidates):
                    break

        return ans[target]


class SolutionDFS(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)