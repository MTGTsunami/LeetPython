# Top K problems

l = [3, 2, 8, 4, 5, 1, 10, 9, 7]


def quickSelect(l, low, high, K):
    if low <= high:
        idx = findPivot(l, low, high)
        if idx == len(l) - K:
            return l[idx]
        elif idx > len(l) - K:
            return quickSelect(l, low, idx - 1, K)
        else:
            return quickSelect(l, idx + 1, high, K)


def findPivot(l, low, high):
    pivot = l[low]
    while low < high:
        while low < high and l[high] >= pivot:
            high -= 1
        l[low] = l[high]

        while low < high and l[low] <= pivot:
            low += 1
        l[high] = l[low]
    l[low] = pivot
    return low


for i in range(1, len(l) + 1):
    print(quickSelect(l, 0, len(l) - 1, i))
