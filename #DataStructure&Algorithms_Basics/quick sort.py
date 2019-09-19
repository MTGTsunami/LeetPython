l = [3, 2, 8, 4, 5, 1, 10, 9, 7]

def getIndex(l, low, high):
    temp = l[low]

    while low < high:
        while l[high] >= temp and low < high:
            high -= 1
        l[low] = l[high]

        while l[low] <= temp and low < high:
            low += 1
        l[high] = l[low]

    index = low
    l[index] = temp

    return index

def quickSort(l, low, high):
    if low < high:
        index = getIndex(l, low, high)
        quickSort(l, low, index - 1)
        quickSort(l, index + 1, high)


print(l)
quickSort(l, 0, len(l) - 1)
print(l)


