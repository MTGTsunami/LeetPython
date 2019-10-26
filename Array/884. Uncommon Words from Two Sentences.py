"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""

from collections import Counter


class MySolution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ca = Counter(A.split(" "))
        cb = Counter(B.split(" "))
        if not A:
            ca = {}
        if not B:
            cb = {}

        res = []
        for word in ca.keys():
            if ca[word] == 1 and word not in cb:
                res.append(word)
        for word in cb.keys():
            if cb[word] == 1 and word not in ca:
                res.append(word)
        return res
