"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""

from collections import defaultdict


class Solution:  # Tarjan algorithm
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        res, low, graph = [], [-1] * n, defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(timestamp, curr_node, parent_node):
            dfn, low[curr_node] = timestamp, timestamp
            for node in graph[curr_node]:
                if node != parent_node:
                    if low[node] == -1:
                        timestamp += 1
                        dfs(timestamp, node, curr_node)
                        if low[node] > dfn:
                            res.append([curr_node, node])
                    low[curr_node] = min(low[curr_node], low[node])

        dfs(0, 0, -1)
        return res