def max_bpm(graph):
    def bpm(u, seen):
        for v in range(len(graph[0])):
            if graph[u][v] == 1 and not seen[v]:
                seen[v] = True
                if match[v] == -1 or bpm(match[v], seen):
                    match[v] = u
                    return True
        return False

    match = [-1] * len(graph[0])
    res = 0
    for u in range(len(graph)):
        seen = [False] * len(graph[0])
        if bpm(u, seen):
            res += 1
    return res


if __name__ == '__main__':
    graph = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1]
    ]
    print(max_bpm(graph))
