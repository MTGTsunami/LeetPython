"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

from collections import *


class MySolution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        edge = defaultdict(list)
        indegree = defaultdict(int)
        charset = set()
        for i in range(len(words) - 1):
            ptr = 0
            notOrdered = True
            while ptr < len(words[i]) and ptr < len(words[i + 1]):
                if notOrdered and words[i][ptr] != words[i + 1][ptr]:
                    indegree[words[i][ptr]] += 0
                    indegree[words[i + 1][ptr]] += 1
                    edge[words[i][ptr]].append(words[i + 1][ptr])
                    notOrdered = False
                else:
                    charset.add(words[i][ptr])
                    charset.add(words[i + 1][ptr])
                ptr += 1

            if len(words[i]) < len(words[i + 1]):
                while ptr < len(words[i + 1]):
                    charset.add(words[i + 1][ptr])
                    ptr += 1
            else:
                while ptr < len(words[i]):
                    charset.add(words[i][ptr])
                    ptr += 1

        for char in indegree.keys():
            if char in charset:
                charset.remove(char)
        noTopoOrder = ""
        for char in charset:
            noTopoOrder += char

        topo = deque()
        visited = set()
        out = ""
        for k, v in indegree.items():
            if v == 0:
                topo.append(k)
                visited.add(k)
        while topo:
            kahn = topo.popleft()
            out += kahn
            for vertice in edge[kahn]:
                indegree[vertice] -= 1
            for k, v in indegree.items():
                if v == 0 and k not in visited:
                    topo.append(k)
                    visited.add(k)

        if len(visited) == len(indegree):
            return out + noTopoOrder
        else:
            return ""


class SolutionDFS:
    def add_vertices(self, w, graph):
        for ch in w:
            if ch not in graph:
                graph[ch] = set([])
        return

    def add_words_to_graph(self, graph, w1, w2):
        self.add_vertices(w1, graph)
        self.add_vertices(w2, graph)
        min_length = min(len(w1), len(w2))
        found = False
        for i in range(min_length):
            if w1[i] != w2[i]:
                graph[w1[i]].add(w2[i])
                found = True
                break
        if found == False and len(w1) > len(w2):
            return False  # "abstract", "abs" is an error. But "abs", "abstract" is perfectly fine.
        return True

    def build_graph(self, words):
        graph = {}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if not self.add_words_to_graph(graph, w1, w2):
                return {}
        self.add_vertices(words[-1], graph)
        return graph

    def topo_dfs(self, x, g, visited, visiting, st):  # Return True if there is a cycle
        visited.add(x)
        visiting.add(x)
        for nbr in g[x]:
            if nbr in visiting:  # Back-Edge!
                return True
            if nbr not in visited:
                if self.topo_dfs(nbr, g, visited, visiting, st):
                    return True
        visiting.remove(x)
        st.append(x)
        return False

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words == []:
            return ""
        graph = self.build_graph(words)
        visited, visiting, st = set([]), set([]), []
        for k in graph.keys():
            if k not in visited:
                if self.topo_dfs(k, graph, visited, visiting, st):
                    return ""
        st.reverse()
        return "".join(st)


from collections import *


class SolutionKAHN:
    def alienOrder(self, words):
        # a -> b
        adj = defaultdict(set)
        # in-degree
        deg = {c: 0 for w in words for c in w}
        for i, w1 in enumerate(words[:-1]):
            w2 = words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 == c2: continue
                if c2 not in adj[c1]: deg[c2] += 1
                adj[c1].add(c2)
                break
        res = ''
        # start w 0 indegree nodes
        q = deque([c for c in deg if not deg[c]])
        while q:
            c = q.popleft()
            res += c
            for n in adj[c]:
                deg[n] -= 1
                if not deg[n]: q.append(n)
        return res if len(res) == len(deg) else ''