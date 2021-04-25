"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.

Example:

Input:
n: 13   k: 2

Output:
10

Explanation:
The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""


class Solution(object):  # 十叉树
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        def stepFinder(n, n1, n2):
            step = 0
            while n1 <= n:
                step += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return step

        curr = 1
        k -= 1
        while k > 0:
            step = stepFinder(n, curr, curr + 1)
            if k >= step:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        return curr


"""
Actually this is a denary tree (each node has 10 children). Find the kth element is to do a k steps preorder traverse of the tree.
0_1477293053966_upload-40379731-118a-4753-bed9-1cb372790d4b

Initially, image you are at node 1 (variable: curr),
the goal is move (k - 1) steps to the target node x. (substract steps from k after moving)
when k is down to 0, curr will be finally at node x, there you get the result.

we don't really need to do a exact k steps preorder traverse of the denary tree, the idea is to calculate the steps between curr and curr + 1 (neighbor nodes in same level), in order to skip some unnecessary moves.

Main function
Firstly, calculate how many steps curr need to move to curr + 1.

if the steps <= k, we know we can move to curr + 1, and narrow down k to k - steps.

else if the steps > k, that means the curr + 1 is actually behind the target node x in the preorder path, we can't jump to curr + 1. What we have to do is to move forward only 1 step (curr * 10 is always next preorder node) and repeat the iteration.

calSteps function

how to calculate the steps between curr and curr + 1?
Here we come up a idea to calculate by level.
Let n1 = curr, n2 = curr + 1.
n2 is always the next right node beside n1's right most node (who shares the same ancestor "curr")
(refer to the pic, 2 is right next to 1, 20 is right next to 19, 200 is right next to 199).

so, if n2 <= n, what means n1's right most node exists, we can simply add the number of nodes from n1 to n2 to steps.

else if n2 > n, what means n (the biggest node) is on the path between n1 to n2, add (n + 1 - n1) to steps.

organize this flow to "steps += math.min(n + 1, n2) - n1; n1 *= 10; n2 *= 10;"
"""