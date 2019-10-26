"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

from collections import Counter


class MySolution(object):  # Counter is kind of slow
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        res = []
        count = Counter(p)
        compare = {}
        for i in range(len(s) - len(p) + 1):
            if not compare:
                compare = Counter(s[i:i + len(p)])
            else:
                compare[s[i - 1]] -= 1
                if compare[s[i - 1]] == 0:
                    del compare[s[i - 1]]

                if s[i + len(p) - 1] not in compare:
                    compare[s[i + len(p) - 1]] = 1
                else:
                    compare[s[i + len(p) - 1]] += 1

            if compare == count:
                res.append(i)
        return res
