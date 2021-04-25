"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""


class MySolution1(object):  # o(n^2*k) time TLE
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def isPalindrome(s):
            n = len(s)
            l, r = (n - 1) // 2, (n - 1) // 2 + (n - 1) % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if l >= 0:
                return False
            else:
                return True

        output = []
        if not words:
            return output

        m = len(words)
        for i in range(m):
            for j in range(m):
                if i != j:
                    if isPalindrome(words[i] + words[j]):
                        output.append([i, j])
        return output


class MySolution2(object):  # O(n*k^2) time PASS but beats 6.83% in time and 88.93% in space
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words:
            return []

        output = []
        wordset = set(words)
        for i, word in enumerate(words):
            word = '#' + '#'.join(word) + '#'
            n = len(word)
            for j in range(n):
                l, r = j, j
                tillEnd = True
                firstHalf = False
                while l >= 0 and r < n:
                    if word[l] != word[r]:
                        tillEnd = False
                        break
                    l -= 1
                    r += 1

                if tillEnd:
                    if j >= n // 2:
                        remain = word[:(j - n // 2) * 2][::-1]
                    else:
                        remain = word[2 * j + 1:][::-1]
                        firstHalf = True
                    remain = remain.replace("#", "")
                    if remain in wordset:
                        k = words.index(remain)
                        if i != k:
                            if firstHalf:
                                if [k, i] not in output:
                                    output.append([k, i])
                            else:
                                if [i, k] not in output:
                                    output.append([i, k])
                                    if remain == "":
                                        output.append([k, i])
        return output


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {w: i for i, w in enumerate(words)}
        ans = []
        for i, w in enumerate(words):
            # no divide, two cases
            if w[::-1] in d and d[w[::-1]] != i:
                ans.append([i, d[w[::-1]]])
            if w != '' and w[::-1] == w and '' in d:
                ans.append([i, d['']])
                ans.append([d[''], i])

            # divide into two parts, can't be self, another two cases
            for k in range(1, len(w)):
                s1, s2 = w[:k], w[k:]
                if s1 == s1[::-1] and s2[::-1] in d:
                    ans.append([d[s2[::-1]], i])
                if s2 == s2[::-1] and s1[::-1] in d:
                    ans.append([i, d[s1[::-1]]])
        return ans






