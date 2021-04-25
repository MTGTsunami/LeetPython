"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0

        tempRightMax = -1
        tempLeftMax = height[0]
        water = 0
        for h in height[1:]:
            tempRightMax = max(tempRightMax, h)

        for i in range(1, n):
            tempLeftMax = max(tempLeftMax, height[i])
            water += (min(tempLeftMax, tempRightMax) - height[i])
            print(water)
            if height[i] == tempRightMax:
                tempRightMax = -1
                for j in range(i + 1, n):
                    tempRightMax = max(tempRightMax, height[j])

        return water