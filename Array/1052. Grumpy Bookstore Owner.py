"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
"""


class MySolution:  # Greedy
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        unsatisfied = []
        countCustomer, countUnsatisfied, firstX = 0, 0, 0
        for i, g in enumerate(grumpy):
            countCustomer += customers[i]
            if g == 1:
                unsatisfied.append(customers[i])
                countUnsatisfied += customers[i]
            else:
                unsatisfied.append(0)
            if i < X:
                firstX += unsatisfied[i]

        maxUnsatisfied = firstX
        if X <= len(unsatisfied):
            l, r = 0, X - 1
            while r < len(unsatisfied) - 1:
                r += 1
                firstX = firstX - unsatisfied[l] + unsatisfied[r]
                maxUnsatisfied = max(maxUnsatisfied, firstX)
                l += 1

        return countCustomer if X > len(unsatisfied) else countCustomer - countUnsatisfied + maxUnsatisfied




