"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""


class SolutionDP(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # dp[i][j] stands for the minimum value of the largest sum among these j subarrays
        # from the first element in nums to the ith element in nums.

        n = len(nums)
        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        presum = [0] * (n + 1)
        for i, num in enumerate(nums):
            presum[i + 1] = num + presum[i]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], presum[i] - presum[k]))
        return dp[n][m]


class Solution_binarySearch(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l, r = 0, 0
        n = len(nums)
        for i in range(n):
            r += nums[i]
            if l < nums[i]:
                l = nums[i]

        ans = r
        while l <= r:
            mid = (l + r) // 2  # mid = (l + r) >> 1
            summ, cut = 0, 1
            for i in range(n):
                if summ + nums[i] > mid:
                    cut += 1
                    summ = nums[i]
                else:
                    summ += nums[i]

            if cut <= m:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans



"""
Intuition

We can easily find a property for the answer:

If we can find a splitting method that ensures the maximum largest subarray sum will not exceed a value x, then we can also find a splitting method that ensures the maximum largest subarray sum will not exceed any value y that is greater than x.

Lets define this property as F(x) for the value x. F(x) is true means we can find a splitting method that ensures the maximum largest subarray sum will not exceed x.

From the discussion above, we can find out that for x ranging from -INFINITY to INFINITY, F(x) will start with false, then from a specific value x0, F(x) will turn to true and stay true forever.

Obviously, the specific value x0 is our answer.

Algorithm

We can use Binary search to find the value x0. Keeping a value mid = (left + right) / 2. If F(mid) is false, then we will search the range [mid + 1, right]; If F(mid) is true, then we will search [left, mid - 1].

For a given x, we can get the answer of F(x) using a greedy approach. Using an accumulator sum to store the sum of the current processing subarray and a counter cnt to count the number of existing subarrays. We will process the elements in the array one by one. For each element num, if sum + num <= x, it means we can add num to the current subarray without exceeding the limit. Otherwise, we need to make a cut here, start a new subarray with the current element num. This leads to an increment in the number of subarrays.

After we have finished the whole process, we need to compare the value cnt to the size limit of subarrays m. If cnt <= m, it means we can find a splitting method that ensures the maximum largest subarray sum will not exceed x. Otherwise, F(x) should be false.
"""