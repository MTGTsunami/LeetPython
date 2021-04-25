"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

import collections
# MySolution


class TrieNode(object):

    def __init__(self):
        self.link = collections.defaultdict(TrieNode)
        self.isEnd = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.link[char]
        node.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def find(word, node):
            for i, char in enumerate(word):
                if char == '.':
                    for key in node.link.keys():
                        if find(word[i + 1:], node.link[key]):
                            return True
                    return False
                else:
                    if char not in node.link:
                        return False
                    node = node.link[char]
            return node.isEnd

        return find(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)