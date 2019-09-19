"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class SolutionDFS(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True


"""
拓扑排序算法 ：
一、 Kahn算法
本质是减治法，步骤是

1.找到所有入度为0的的顶点
2.这些顶点入栈
3.出栈，输出，并删除该顶点的出边，回到第 1 步
按这个次序输出的就是拓扑序列了。

二. 基于dfs的拓扑排序
与dfs算法本身有一定的区别，是通过dfs算法的顺序去遍历顶点，但是输出拓扑排序的时候是需要新的顺序的。
dfs的顺序，第一个顶点，第一个顶点的其中一个邻顶点，然后是不断的访问下一个邻顶点，直到没有之后，返回第一个顶点，访问其未访问过的邻顶点。
显然，这样是不符合拓扑排序的顺序的，所以，我们在使用dfs进行拓扑排序的时候，进行了修改。
此时的顺序是，dfs访问顺序，但是其访问的第一个结点是最深的结点，接着是最深结点的上一个结点，一直到第一个结点，不访问第一个结点，而是进而向第一个结点的未被访问的邻结点开始访问这一方向的最深结点。直到第一个结点的所有邻结点都被访问了，在访问第一个结点。
可递归调用dfs。
"""
class SolutionBFS(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        G = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses