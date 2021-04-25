"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.





The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0 or n == 1:
            return 0

        ptr1 = 0
        ptr2 = n - 1
        maxWater = 0
        while ptr1 != ptr2:
            if height[ptr1] <= height[ptr2]:
                water = height[ptr1] * (ptr2 - ptr1)
                ptr1 += 1
            else:
                water = height[ptr2] * (ptr2 - ptr1)
                ptr2 -= 1

            if water > maxWater:
                maxWater = water

        return maxWater

