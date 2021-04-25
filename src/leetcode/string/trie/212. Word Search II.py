"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""


class TrieNode(object):
    def __init__(self):
        self.link = collections.defaultdict(TrieNode)
        self.isEnd = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            # node.link[char] = TrieNode()  No need for this due to defaultdict
            node = node.link[char]
        node.isEnd = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.link[char]
            if not node:
                return False
        return node.isEnd


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        row = len(board)
        col = len(board[0])
        trie = Trie()
        node = trie.root

        for word in words:
            trie.insert(word)

        for i in range(row):
            for j in range(col):
                self.dfs(ans, node, i, j, "", board)
        return ans

    def dfs(self, ans, node, i, j, path, board):
        if node.isEnd:
            ans.append(path)
            node.isEnd = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        temp = board[i][j]
        node = node.link.get(temp)  # cannot write "node = node.link[temp]", which will cause MLE
        if not node:
            return

        board[i][j] = "#"
        self.dfs(ans, node, i - 1, j, path + temp, board)
        self.dfs(ans, node, i + 1, j, path + temp, board)
        self.dfs(ans, node, i, j - 1, path + temp, board)
        self.dfs(ans, node, i, j + 1, path + temp, board)
        board[i][j] = temp
