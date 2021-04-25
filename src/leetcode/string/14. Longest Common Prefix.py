"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):  # Horizontal scanning
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ""

        ins = strs[0]
        index = len(ins)

        for i in range(1, n):
            while True:
                if len(ins[:index]) > len(strs[i]):
                    index = len(strs[i])

                if ins[:index] != strs[i][:index]:
                    index -= 1
                else:
                    break

                if index <= 0:
                    return ""

        return ins[:index]


class TrieNode(object):
    def __init__(self):
        self.isEnd = False
        self.links = collections.defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.links[char]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.links[char]
            if not node:
                return False
        return node.isEnd


class SolutionTrie(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        trie = Trie()
        for string in strs:
            trie.insert(string)

        depth = 0
        node = trie.root
        while len(node.links) == 1 and not node.isEnd:
            node = node.links[strs[0][depth]]
            depth += 1
        return strs[0][:depth]

