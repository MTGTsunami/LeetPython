"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""


class SolutionGreedy(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans


class MySolution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        maxindex = 0
        ptr = 0
        temp = 0

        while ptr < len(S):
            if ptr > maxindex:
                if not ans:
                    ans.append(ptr)
                else:
                    ans.append(ptr - temp)
                temp = ptr

            char = S[ptr]
            if S[ptr] == "#":
                ptr += 1
                continue

            while S.find(char) != -1:
                index = S.find(char)
                S = S.replace(char, "#", 1)

            maxindex = max(maxindex, index)
            ptr += 1

        ans.append(ptr - temp)
        return ans