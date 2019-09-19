# Thumbtack OA1
# followup1：有重复点怎么办
# followup2：如果输入是double 并且有误差范围怎么办
# followup3：如果不要求平行于y轴 怎么办
"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:

Input: [[1,1],[-1,1]]
Output: true
Example 2:

Input: [[1,1],[-1,-1]]
Output: false
Follow up:
Could you do better than O(n2) ?
"""


class MySolution(object):  # O(nlgn)
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True

        pset = set()
        for i in range(len(points)):
            points[i] = tuple(points[i])
            pset.add(points[i])
        points = list(pset)

        hasAxis = False
        points.sort(key=lambda x: (x[1], x[0]))
        l, r = 0, 0
        curr = points[0][1]
        while r < len(points):
            while r < len(points) and points[r][1] == curr:
                r += 1
            count = r - l - 1
            for i in range(count // 2 + 1):
                newaxis = float(points[l + i][0] + points[r - 1 - i][0]) / 2
                if not hasAxis:
                    axis = newaxis
                    hasAxis = True
                else:
                    if axis != newaxis:
                        return False
            l = r
            if r < len(points):
                curr = points[r][1]
        return True


# 图中的edge和坐标点均可以保存在字典当中
from collections import defaultdict


class Solution(object):  # 有问题， 需要将同样的坐标剔除
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 1:
            return True

        y_coord = defaultdict(list)
        for x, y in sorted(points, key=lambda x: x[0]):
            y_coord[y].append(x)

        y_axis = None
        for y, x in y_coord.items():
            for i in range(len(x) / 2 + 1):
                cur_y_axis = float(x[i] + x[len(x) - 1 - i]) / 2
                if not y_axis:
                    y_axis = cur_y_axis
                else:
                    if y_axis != cur_y_axis:
                        return False
        return True
