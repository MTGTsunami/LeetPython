"""
Given n, how many structurally unique bst's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique bst's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0] * (n + 1)
        G[0] = 1
        G[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[-1]


"""
The problem can be solved in a dynamic programming way.
Given a sorted sequence 1 ... n, to construct a Binary Search Tree (bst) out of the sequence, 
we could enumerate each number i in the sequence, and use the number as the root, 
then, the subsequence 1 ... (i-1) on its left side would lay on the left branch of the root, 
and similarly the right subsequence (i+1) ... n lay on the right branch of the root. 
We then can construct the subtree from the subsequence recursively. 
Through the above approach, we could be assured that the bst that we construct are all unique, since they start from unique roots.

As we can see, the problem can be reduced into problems with smaller sizes, 
instead of recursively (also repeatedly) solve the subproblems, 
we can store the solution of subproblems and reuse them later, i.e. the dynamic programming way.

Algorithm:
The problem is to calculate the number of unique bst. To do so, we can define two functions:
G(n): the number of unique bst for a sequence of length n.
F(i, n): the number of unique bst, where the number i is served as the root of bst (1≤i≤n).

As we can see,
G(n)is actually the desired function we need in order to solve the problem.
Later we would see that G(n) can be deducted from F(i, n)F(i,n), which at the end, would recursively refers to G(n).

First of all, following the idea in the section of intuition, we can see that the total number of unique bst G(n), 
is the sum of bst F(i, n) enumerating each number i (1 <= i <= n) as a root. i.e.

G(n) = ∑ (i=1 to n) F(i,n)         (1)

Particularly, for the bottom cases, there is only one combination to construct a bst out of a sequence of length 1 (only a root) or nothing (empty tree). i.e.
G(0) = 1, G(1) = 1

Given a sequence 1 ... n, we pick a number i out of the sequence as the root, 
then the number of unique bst with the specified root defined as F(i, n), 
is the cartesian product of the number of bst for its left and right subtrees, as illustrated below:

For example, F(3, 7), the number of unique bst tree with the number 3 as its root. 
To construct an unique bst out of the entire sequence [1, 2, 3, 4, 5, 6, 7] with 3 as the root, 
which is to say, we need to construct a subtree out of its left subsequence [1, 2] and another subtree out of the right subsequence [4, 5, 6, 7], 
and then combine them together (i.e. cartesian product). 
Now the tricky part is that we could consider the number of unique bst out of sequence [1,2] as G(2),
and the number of of unique bst out of sequence [4, 5, 6, 7] as G(4). 
For G(n), it does not matter the content of the sequence, but the length of the sequence. 
Therefore, F(3,7) = G(2) * G(4). To generalise from the example, we could derive the following formula:

F(i,n) = G(i−1) ⋅ G(n−i)            (2)
By combining the formulas (1), (2), we obtain a recursive formula for G(n), i.e.
G(n)=∑ (i=1 to n) G(i−1)⋅G(n−i)    (3)

To calculate the result of function, we start with the lower number, 
since the value of G(n) depends on the values of G(0) … G(n-1).
With the above explanation and formulas, one can easily implement an algorithm to calculate the G(n). 
"""