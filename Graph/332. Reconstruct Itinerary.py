"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
But it is larger in lexical order.
"""

from collections import defaultdict


class MySolution(object):  # Backtracking
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        flights = defaultdict(list)
        for start, end in tickets:
            flights[start].append(end)

        def dfs(start, res):
            if len(res) == len(tickets) + 1:
                return res
            if start not in flights:
                return
            for i, des in enumerate(sorted(flights[start])):
                res.append(des)
                flights[start].remove(des)
                out = dfs(des, res)
                if out:
                    return out
                res.pop()
                flights[start].append(des)

        return dfs("JFK", ["JFK"])


from collections import defaultdict


class Solution(object):  # simple dfs
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        flights = defaultdict(list)
        for start, end in sorted(tickets)[::-1]:
            flights[start].append(end)

        route = []

        def visit(airport):
            while flights[airport]:
                visit(flights[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]
