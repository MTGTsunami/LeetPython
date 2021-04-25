"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""


class MyBFS_Solution1(object):  # TLE from case 33, 无剪枝函数
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        i = -1
        destination = set()
        destination.add((src, 0))
        final = []
        while i < K:
            newDes = set()
            i += 1
            for city in destination:
                for data in flights:
                    if data[0] == city[0]:
                        arrive = (data[1], city[1] + data[2])
                        if data[1] != dst:
                            newDes.add(arrive)
                        else:
                            final.append(arrive)
            destination = newDes

        if not final:
            return -1

        minCost = float("inf")
        for des in final:
            minCost = min(minCost, des[1])
        return minCost


class MyBFS_Solution2(object):  # Pass, 带剪枝判断
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        i = 0
        destination = set()
        destination.add((src, 0))
        cheapest = [float("inf")] * n
        while i <= K:
            newDes = set()
            i += 1
            for city in destination:
                for data in flights:
                    if data[0] == city[0]:
                        if data[1] != dst:
                            if city[1] + data[2] < cheapest[data[1]]:
                                cheapest[data[1]] = city[1] + data[2]
                                newDes.add((data[1], city[1] + data[2]))
                        else:
                            cheapest[dst] = min(cheapest[dst], city[1] + data[2])
            destination = newDes

        if cheapest[dst] == float("inf"):
            return -1
        else:
            return cheapest[dst]


"""
这里我们使用一个二维DP数组，其中dp[i][j]表示最多飞i次航班到达j位置时的最少价格，
那么dp[0][src]初始化为0，因为飞0次航班的价格都为0，转机K次，其实就是飞K+1次航班，
我们开始遍历，i从1到K+1，每次dp[i][src]都初始化为0，因为在起点的价格也为0，然后即使遍历所有的航班x，更新dp[i][x[1]]，
表示最多飞i次航班到达航班x的目的地的最低价格，用最多飞i-1次航班，
到达航班x的起点的价格加上航班x的价格之和，二者中取较小值更新即可.
"""
class SolutionDP(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dp = [[float("inf") for _ in range(n)] for _ in range(K + 2)]
        dp[0][src] = 0
        for i in range(1, K + 2):
            dp[i][src] = 0
            for u, v, w in flights:
                dp[i][v] = min(dp[i][v], dp[i - 1][u] + w)
        return -1 if dp[K + 1][dst] == float("inf") else dp[K + 1][dst]


class SolutionHeap_Dijkstra(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K+1 or cost > best.get((k, place), float('inf')): continue
            if place == dst: return cost

            for nei, wt in graph[place].iteritems():
                newcost = cost + wt
                if newcost < best.get((k+1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k+1, nei))
                    best[k+1, nei] = newcost

        return -1