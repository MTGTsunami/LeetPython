"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

import copy
from collections import defaultdict


class MyDFS_Solution(object):  # TLE case 19
    def __init__(self):
        self.minlen = float("inf")

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        def dfs(node, visited):
            word, route = node[0], node[1]
            if word == endWord:
                self.minlen = min(self.minlen, len(route))
                routes.append(copy.deepcopy(route))
                return
            for i in range(n):
                mid = word[:i] + "*" + word[i + 1:]
                if mid in midState:
                    for state in midState[mid]:
                        if state not in visited:
                            route.append(state)
                            visited.add(state)
                            dfs((state, route), visited)
                            route.pop()
                            visited.remove(state)

        if not beginWord or not endWord or not wordList:
            return []

        midState = defaultdict(list)
        n = len(wordList[0])
        for word in wordList:
            for i in range(n):
                midState[word[:i] + "*" + word[i + 1:]].append(word)

        visited = set()
        visited.add(beginWord)
        routes = []
        dfs((beginWord, [beginWord]), visited)

        out = []
        for route in routes:
            if len(route) == self.minlen:
                out.append(route)
        return out


from collections import *


class MyBFS_Solution(object):  # TLE at case 21

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not beginWord or not endWord or not wordList:
            return []

        n = len(wordList[0])
        wordList = set(wordList)
        start = OrderedDict()
        start[beginWord] = ""

        minlen, firstReached = float("inf"), False
        out = []
        queue = deque([(beginWord, start, 0)])
        while queue:
            word, route, depth = queue.popleft()
            if word == endWord:
                if not firstReached:
                    firstReached = True
                    minlen = depth
                if depth <= minlen:
                    out.append(route.keys())

            if depth < minlen:
                for i in range(n):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        state = word[:i] + c + word[i + 1:]
                        if state in wordList:
                            if state not in route:
                                newRoute = OrderedDict()
                                for k, v in route.items():
                                    newRoute[k] = v
                                newRoute[state] = ""
                                queue.append((state, newRoute, depth + 1))

        return out


class Solution(object):  # layer BFS

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []

        wordList = set(wordList)
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            state = w[:i] + c + w[i + 1:]
                            if state in wordList:
                                newlayer[state] += [j + [state] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res
