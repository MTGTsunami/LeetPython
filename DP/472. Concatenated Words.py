"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""


class MySolution:  # Inspired by Word Break
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        output = []
        for word in words:
            n = len(word)
            dp = [False] * (n + 1)
            if n:
                dp[0] = True
            wordset.remove(word)

            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordset:
                        dp[i] = True
                        break
            if dp[-1]:
                output.append(word)
            wordset.add(word)

        return output


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        words_dict = set(words)
        for word in words:
            words_dict.remove(word)
            if self.check(word, words_dict) is True:
                res.append(word)
            words_dict.add(word)
        return res

    def check(self, word, d):
        if word in d:
            return True

        for i in range(len(word), 0, -1):
            if word[:i] in d and self.check(word[i:], d):
                return True
        return False

