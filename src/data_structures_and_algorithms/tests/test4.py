from collections import defaultdict

def isReflected(points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    if len(points) == 1:
        return True

    y_coord = defaultdict(list)
    for x, y in sorted(points, key=lambda x: x[0]):
        y_coord[y].append(x)

    y_axis = None
    for y, x in y_coord.items():
        for i in range(len(x) // 2 + 1):
            cur_y_axis = float(x[i] + x[len(x) - 1 - i]) / 2
            if not y_axis:
                y_axis = cur_y_axis
            else:
                if y_axis != cur_y_axis:
                    return False
    return True


print(isReflected([[2,1],[2,1],[4,1]]))