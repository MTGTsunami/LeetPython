"""
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.



Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23


Note:

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9
"""


class MySolution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        count, maxpile = 0, float("-inf")
        for pile in piles:
            count += pile
            maxpile = max(maxpile, pile)
        if count <= H:
            return 1

        l, r = 1, maxpile
        while l < r - 1:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                quo, rem = divmod(pile, mid)
                hours += quo if rem == 0 else quo + 1

            if hours <= H:
                r = mid
            else:
                l = mid
        return r
