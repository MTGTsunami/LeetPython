def Q3(projectsInfo, projectsTimeRanges, prosInfo, prosTimeRanges):
    graph = [[0] * len(prosInfo) for _ in range(len(projectsInfo))]
    print(graph)
    sizeDict = {0: 120, 1: 240, 2: 360}
    for i, pj in enumerate(projectsInfo):
        x1, y1, budget, size = pj[0], pj[1], pj[2], pj[3]
        pjTR = []
        for time in projectsTimeRanges[i]:
            start, end = time.split('-')
            hourS, minS = start.split(':')
            hourE, minE = end.split(':')
            pjTR.append((int(hourS)*60+int(minS), int(hourE)*60+int(minE)))

        for j, pro in enumerate(prosInfo):
            x2, y2, rate = pro[0], pro[1], pro[2]
            if budget >= rate:
                distance = abs(x2 - x1) + abs(y2 - y1)
                found = False
                for time in prosTimeRanges[j]:
                    start, end = time.split('-')
                    hourS, minS = start.split(':')
                    hourE, minE = end.split(':')
                    endTime = int(hourS) * 60 + int(minS) + distance + sizeDict[size]
                    if endTime <= int(hourE) * 60 + int(minE):
                        l, r = 0, len(pjTR) - 1
                        while l <= r:
                            mid = (l + r) // 2
                            if pjTR[mid][0] < endTime:
                                if pjTR[mid][1] >= endTime:
                                    graph[i][j] = 1
                                    found = True
                                    break
                                else:
                                    l = mid + 1
                            elif pjTR[mid][0] > endTime:
                                r = mid - 1
                            else:
                                graph[i][j] = 1
                                found = True
                                break
                        if found:
                            break

    return maxBGMatching(graph)


def maxBGMatching(graph):
    def dfs(i):
        for j in range(len(graph[0])):
            if graph[i][j] and not assigned[j]:
                assigned[j] = True
                if match[j] == -1 or dfs(match[j]):
                    return True
        return False

    match = [-1] * len(graph[0])
    maxMatch = 0
    for i in range(len(graph)):
        assigned = [False] * len(graph[0])
        if dfs(i):
            maxMatch += 1
    return maxMatch


print(Q3([[0, 0, 5, 0], [1, 2, 8, 1], [-2, 1, 10, 2]],
         [["08:00-10:30", "11:59-14:00", "20:30-23:05"], ["16:30-21:00"], ["00:00-23:59"]],
         [[5, 0, 7], [0, 1, 5], [-1, -1, 8]],
         [["10:00-16:06"], ["11:50-14:00", "20:30-23:07"], ["17:00-23:30"]]
))


print(Q3([[0, 0, 5, 0], [1, 2, 8, 1], [-2, 1, 10, 2]],
         [["08:00-10:30", "11:59-14:00", "20:30-23:05"], ["16:30-21:00"], ["00:00-23:59"]],
         [[5, 0, 7], [0, 1, 5], [-1, -1, 8]],
         [["10:00-16:06"], [], ["17:00-23:30"]]
))

