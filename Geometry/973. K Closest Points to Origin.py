"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""


class SolutionSort(object):  # O(nlogn)
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:K]

import heapq


class Solution(object):  # O(nlogK) heap
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(K, points, lambda x, y: x * x + y * y)


class MySolution:  # O(n) quick select
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda x: points[x][0] ** 2 + points[x][1] ** 2

        def partition(points, low, high):
            pivot = dist(low)
            pivotPoint = points[low]

            while low < high:
                while low < high and dist(high) >= pivot:
                    high -= 1
                points[low] = points[high]

                while low < high and dist(low) <= pivot:
                    low += 1
                points[high] = points[low]

            points[low] = pivotPoint
            return low

        def quickselect(points, low, high, K):
            if low <= high:
                idx = partition(points, low, high)
                if idx < K - 1:
                    quickselect(points, idx + 1, high, K)
                elif idx > K - 1:
                    quickselect(points, low, idx - 1, K)

        quickselect(points, 0, len(points) - 1, K)
        return points[:K]
