"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""


class MySolution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minute = []
        for time in timePoints:
            h, m = time.split(":")
            minute.append(int(h) * 60 + int(m))
        minute.sort()

        mindiff = float("inf")
        for i in range(1, len(minute)):
            mindiff = min(mindiff, minute[i] - minute[i - 1])
        mindiff = min(mindiff, 24 * 60 + minute[0] - minute[-1])
        return mindiff
