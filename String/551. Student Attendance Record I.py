"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""

class MySolution:
    def checkRecord(self, s: str) -> bool:
        countA, countL = 0, 0
        continuous = False
        for ch in s:
            if ch == "A":
                countA += 1
                continuous = False
                countL = 0
                if countA == 2:
                    return False
            elif ch == "L":
                countL += 1
                continuous = True
                if countL == 3 and continuous:
                    return False
            else:
                continuous = False
                countL = 0
        return True
