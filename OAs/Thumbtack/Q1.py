def PMS(pros, k):
    max_distance = 0
    for pro in pros:
        max_distance = max(max_distance, pro[0])

    idxList = []
    for i, pro in enumerate(pros):
        pms = (max_distance - pro[0]) * pro[1]
        idxList.append((pms, i))

    out = []
    for _, i in sorted(idxList, key=lambda x: x[0], reverse=True)[:k]:
        out.append(i)
    return out


print(PMS([[5, 4], [4, 3], [6, 5], [3, 5]], 2))


